# **FastAPI JWT Authentication System**

A scalable and secure user authentication system built with **FastAPI** and **MongoDB**. This project implements JWT-based authentication, user CRUD operations, and Role-Based Access Control (RBAC).

---

## **Features**

- Secure login and logout endpoints
- Protected user CRUD operations
- Role-Based Access Control (RBAC)
- Logging support across the API
- Modular and scalable code structure
- Configured for MongoDB Atlas (online database)
- Integrated with FastAPI's built-in documentation

---

## **Technologies Used**

- FastAPI
- PyMongo
- JWT
- Pydantic
- MongoDB Atlas
- Uvicorn

---

## **Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/fastapi-jwt-auth.git
   cd fastapi-jwt-auth
Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Set up environment variables:

Create a .env file in the project root directory with the following content:

MONGO_URI=<Your MongoDB Atlas URI>
JWT_SECRET_KEY=<Your Secret Key>
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
Replace <Your MongoDB Atlas URI> and <Your Secret Key> with your credentials.

Create an admin user:

Run the provided script to add a default admin user to the database:

python scripts/create_user.py
This will create a user with the following credentials:

Email: admin@example.com
Password: securepassword
Start the server:

Run the FastAPI server with Uvicorn:

uvicorn app.main:app --reload
The application will be available at http://127.0.0.1:8000, and API documentation at http://127.0.0.1:8000/docs.

