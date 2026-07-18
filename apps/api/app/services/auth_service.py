from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_and_update_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


DUMMY_PASSWORD_HASH = get_password_hash("nat1-invalid-user-password")
MAX_PASSWORD_CHARACTERS = 128


class EmailAlreadyRegisteredError(Exception):
    pass


class AuthService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.users = UserRepository(db)

    def register_user(self, user_create: UserCreate) -> User:
        email = str(user_create.email).lower()
        if self.users.get_by_email(email) is not None:
            raise EmailAlreadyRegisteredError

        user = self.users.create(
            name=user_create.name.strip(),
            email=email,
            password_hash=get_password_hash(user_create.password),
        )

        try:
            self.db.commit()
        except IntegrityError as exc:
            self.db.rollback()
            raise EmailAlreadyRegisteredError from exc

        self.db.refresh(user)
        return user

    def authenticate_user(self, email: str, password: str) -> User | None:
        user = self.users.get_by_email(email.lower())
        password_is_too_long = len(password) > MAX_PASSWORD_CHARACTERS
        password_hash = (
            user.password_hash
            if user is not None and user.is_active
            else DUMMY_PASSWORD_HASH
        )
        is_legacy_bcrypt = password_hash.startswith(("$2a$", "$2b$", "$2y$"))
        legacy_password_exceeds_bcrypt_limit = (
            is_legacy_bcrypt and len(password.encode("utf-8")) > 72
        )
        password_to_verify = (
            "nat1-invalid-overlong-password"
            if password_is_too_long or legacy_password_exceeds_bcrypt_limit
            else password
        )
        password_matches, replacement_hash = verify_and_update_password(
            password_to_verify,
            password_hash,
        )

        if (
            user is None
            or not user.is_active
            or password_is_too_long
            or legacy_password_exceeds_bcrypt_limit
            or not password_matches
        ):
            return None

        if replacement_hash is not None:
            user.password_hash = replacement_hash
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)

        return user

    def get_user_by_id(self, user_id: UUID) -> User | None:
        return self.users.get_by_id(user_id)
