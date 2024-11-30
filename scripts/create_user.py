from app.services.auth_service import create_user

if __name__ == "__main__":
    email = "admin@example.com"
    full_name = "Admin User"
    password = "securepassword"
    role = "admin"
    create_user(email, full_name, password, role)
    print(f"Admin user {email} created successfully.")
