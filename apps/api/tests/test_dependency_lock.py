from pathlib import Path

from packaging.requirements import Requirement
from packaging.utils import canonicalize_name


API_ROOT = Path(__file__).resolve().parents[1]


def load_requirements(path: Path) -> list[Requirement]:
    return [
        Requirement(line)
        for raw_line in path.read_text(encoding="utf-8").splitlines()
        if (line := raw_line.strip()) and not line.startswith("#")
    ]


def exact_version(requirement: Requirement) -> str:
    specifiers = list(requirement.specifier)
    assert len(specifiers) == 1 and specifiers[0].operator == "==", (
        f"{requirement.name} must use one exact == version"
    )
    return specifiers[0].version


def test_direct_requirements_match_combined_ci_lock() -> None:
    locked = {
        canonicalize_name(requirement.name): exact_version(requirement)
        for requirement in load_requirements(API_ROOT / "requirements.lock")
    }

    for manifest_name in ("requirements.txt", "requirements-dev.txt"):
        for requirement in load_requirements(API_ROOT / manifest_name):
            name = canonicalize_name(requirement.name)
            assert name in locked, f"{name} is absent from requirements.lock"
            assert locked[name] == exact_version(requirement), (
                f"{name} version differs between {manifest_name} and requirements.lock"
            )

    removed_vulnerable_stack = {"python-jose", "ecdsa", "rsa", "pyasn1"}
    assert removed_vulnerable_stack.isdisjoint(locked)
