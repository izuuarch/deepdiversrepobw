from .settings import *  # noqa: F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
    }
}

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "www.bwtechglobal.com",
    "bwtechglobal.com",
]

STATIC_ROOT = BASE_DIR / "staticfiles"  # noqa: F405
