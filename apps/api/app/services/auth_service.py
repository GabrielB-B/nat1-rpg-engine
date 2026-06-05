from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


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
        user = self.users.get_by_email(email)
        if user is None or not user.is_active:
            return None
        if not verify_password(password, user.password_hash):
            return None
        return user

    def get_user_by_id(self, user_id: UUID) -> User | None:
        return self.users.get_by_id(user_id)
