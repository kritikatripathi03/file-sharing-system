from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class FileResponse(BaseModel):
    filename: str
    owner_id: int

class TokenData(BaseModel):
    user_id: int