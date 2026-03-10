"""Admin authentication service."""

import hashlib

from config import AUTH_FILE
from utils.file_handler import load_json, save_json


DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin123"


def _hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def _ensure_auth_file() -> dict:
    """Create default credentials if auth file doesn't exist."""
    auth = load_json(AUTH_FILE)
    if not auth:
        auth = {"username": DEFAULT_USERNAME, "password": _hash(DEFAULT_PASSWORD)}
        save_json(AUTH_FILE, auth)
    return auth


def login() -> bool:
    """Prompt for login. Returns True if authenticated."""
    auth = _ensure_auth_file()

    print("\n╔══════════════════════════════════════╗")
    print("║         🔐 ADMIN LOGIN               ║")
    print("╚══════════════════════════════════════╝")

    for attempt in range(3):
        username = input("  Username: ").strip()
        password = input("  Password: ").strip()

        if username == auth["username"] and _hash(password) == auth["password"]:
            print("  ✅ Login successful!\n")
            return True
        remaining = 2 - attempt
        if remaining > 0:
            print(f"  ❌ Invalid credentials. {remaining} attempt(s) left.\n")

    print("  🚫 Too many failed attempts. Exiting.\n")
    return False


def change_password() -> None:
    """Change admin password."""
    auth = _ensure_auth_file()

    current = input("  Enter current password: ").strip()
    if _hash(current) != auth["password"]:
        print("  ❌ Incorrect current password.\n")
        return

    new_pass = input("  Enter new password: ").strip()
    if len(new_pass) < 4:
        print("  ⚠ Password must be at least 4 characters.\n")
        return

    confirm = input("  Confirm new password: ").strip()
    if new_pass != confirm:
        print("  ❌ Passwords do not match.\n")
        return

    auth["password"] = _hash(new_pass)
    save_json(AUTH_FILE, auth)
    print("  ✅ Password changed successfully!\n")
