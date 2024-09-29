from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from auth import verify_token
from db.models import User
from db import session
from auth import create_access_token
from utils import verify_password
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/")
async def x():
    return {"message": "Hello from Ops User"}

@router.post("/login")
async def admin_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(session.get_db)):
    # Retrieve the user from the database based on the username
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Check if the user is an admin
    if user.user_type != "admin":
        raise HTTPException(status_code=403, detail="Not an admin user")
    
    # Generate an access token for the admin user
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(session.get_db)):
    # Allowed MIME types for uploads
    allowed_types = [
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",  # pptx
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",    # docx
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"         # xlsx
    ]
    
    # Validate the uploaded file type
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    # Save the file to the uploads directory
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    
    return {"info": f"File '{file.filename}' uploaded successfully"}
