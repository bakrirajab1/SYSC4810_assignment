import hashlib
import os
import bcrypt

PASSWORD_FILE = "passwd.txt"

# Hash a password
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

# Save user credentials
def save_credentials(username, password, role="Client"):
    """
    Save a user's credentials (username, hashed password, and role) to the password file.
    """
    hashed_password = hash_password(password)
    with open(PASSWORD_FILE, "a") as file:
        file.write(f"{username},{hashed_password},{role}\n")

# Verify user credentials
def verify_credentials(username, password):
    """
    Verify a user's credentials by checking the username and password against the saved data.
    Returns a tuple: (True, role) if the credentials are valid, (False, None) otherwise.
    """
    try:
        with open(PASSWORD_FILE, "r") as file:
            for line in file:
                stored_username, stored_password, role = line.strip().split(",")
                if username == stored_username and bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                    return True, role
    except FileNotFoundError:
        # If the file doesn't exist, explicitly return failure
        return False, None
    except Exception as e:
        # Catch any unexpected error and fail gracefully
        print(f"Error verifying credentials: {e}")
        return False, None

    # If no match is found, return failure
    return False, None
