from Problem2c import verify_credentials

def login_user(username, password):
    """
    Login the user by verifying credentials.
    Returns a tuple: (success_message, role), or (failure_message, None).
    """
    success, role = verify_credentials(username, password)
    if success:
        return f"Login successful! Role: {role}", role
    else:
        return "Login failed: Invalid username or password.", None
