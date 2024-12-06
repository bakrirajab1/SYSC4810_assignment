from Problem2c import save_credentials

def signup_user(username, password):
    if len(username) < 5:
        return "Username must be at least 5 characters long."
    if len(password) < 8 or len(password) > 12:
        return "Password must be between 8 and 12 characters."
    if not any(char.isupper() for char in password):
        return "Password must include at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must include at least one lowercase letter."
    if not any(char.isdigit() for char in password):
        return "Password must include at least one number."
    if not any(char in "!@#$%^&*" for char in password):
        return "Password must include at least one special character (!@#$%^&*)."

    # Update this line to use save_credentials
    save_credentials(username, password, role="Client")
    return "Signup successful!"
