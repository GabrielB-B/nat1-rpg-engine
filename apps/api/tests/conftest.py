import os


# Loaded before test modules so the application never falls back to a developer
# .env secret during automated tests. CI-provided values remain authoritative.
os.environ.setdefault("ENVIRONMENT", "testing")
os.environ.setdefault(
    "SECRET_KEY",
    "nat1-test-only-hs256-secret-that-is-at-least-sixty-four-bytes-long-0001",
)
