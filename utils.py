from passlib.context import CryptContext
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_file_download_link(filename: str) -> str:
    """Generate a secure download link for a file."""
    # Ensure the uploads directory exists
    uploads_path = os.path.join(os.getcwd(), "uploads")  # Get current working directory
    file_path = os.path.join(uploads_path, filename)

    if os.path.exists(file_path):
        # Assuming you have a route set up in your FastAPI to serve files
        return f"https://yourdomain.com/api/download/{filename}"  # Adjust to your actual domain and route
    else:
        raise FileNotFoundError(f"The file {filename} does not exist.")