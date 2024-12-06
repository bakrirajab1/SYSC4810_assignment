import os
from Problem2c import save_user_credentials

PASSWORD_FILE = "passwd.txt"
COMMON_PASSWORDS_FILE = "common_passwords.txt"

# Proactive Password Checker
def is_password_valid(username, password):
    if len(password) < 8 or len(password) > 12:
        return "Password must be 8-12 characters long."
    if username in password:
        return "Password cannot contain the username."
    if not any(char.islower() for char in password):
        return "Password must include at least one lowercase letter."
    if not any(char.isupper() for char in password):
        return "Password must include at least one uppercase letter."
    if not any(char.isdigit() for char in password):
        return "Password must include at least one number."
    if not any(char in "!@#$%^&*" for char in password):
        return "Password must include at least one special character (!@#$%^&*)."
    if is_common_password(password):
        return "Password is too common. Choose a stronger one."
    return None

def is_common_password(password):
    if not os.path.exists(COMMON_PASSWORDS_FILE):
        return False
    with open(COMMON_PASSWORDS_FILE, "r") as file:
        return password in [line.strip() for line in file.readlines()]

def enroll_user(username, password, role="Client"):
    password_error = is_password_valid(username, password)
    if password_error:
        return f"Enrollment failed: {password_error}"
    save_user_credentials(username, password, role)
    return "User enrolled successfully!"
