from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.models.user import User
from core.hashing import Hashing

def create_new_user(user: UserCreate, db: Session):
   user = User(
      email=user.email,
      password=Hashing.get_password_hash(user.password),
      is_active=True,
   )
   db.add(user)
   db.commit()
   db.refresh(user)
   return user

def get_user_by_email(email: str, db: Session):
   return db.query(User).filter(User.email == email).first()
