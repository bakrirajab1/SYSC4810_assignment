import Problem1c
import Problem2c
import Problem3a
import Problem3b
import Problem4a
import Problem4b

def main():
    print("Welcome to justInvest User Management System")
    while True:
        print("\nSelect an option:")
        print("1. Sign Up")
        print("2. Log In")
        print("3. View Role Permissions")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            result = Problem3a.signup_user(username, password)
            print(result)
        elif choice == "2":  # Log In
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            result, role = Problem4a.login_user(username, password)
            print(result)
            if role:
                print(f"Welcome back, {username}! Your role: {role}")
                print(Problem4b.display_authorized_options(role))
        elif choice == "3":
            role = input("Enter your role (e.g., Client, Admin): ")
            permissions = Problem1c.display_permissions(role)
            print(permissions)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
