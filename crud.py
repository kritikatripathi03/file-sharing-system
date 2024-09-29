from sqlalchemy.orm import Session
from db.models import User
import schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate, is_ops_user: bool = False):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        username=user.username, email=user.email, hashed_password=hashed_password, is_ops_user=is_ops_user
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
