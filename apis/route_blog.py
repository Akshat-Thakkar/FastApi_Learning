from fastapi import APIRouter, Depends, status,HTTPException
from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, ShowBlog, UpdateBlog
from db.session import get_db
from db.repository.blog import create_new_blog, retrieve_blog, update_blog_by_id,delete_blog_by_ID
from typing import List
from db.models.user import User
from apis.route_login import get_current_user


router = APIRouter()

@router.put("/blogs", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    blog = create_new_blog(blog=blog, db=db, author_id=current_user.id)
    return blog


@router.put("/blogs/{id}", response_model=ShowBlog)
def update_blog(id: int, blog: UpdateBlog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    blog = update_blog_by_id(id=id, blog=blog, db=db, author_id=current_user.id)
    if isinstance(blog,dict):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=blog["error"])
    return blog



@router.get("/blogs/{blog_id}", response_model=ShowBlog)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=blog_id, db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this ID not found")
    return blog


@router.delete("/blogs/{id}")
def delete_blog(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    message = delete_blog_by_ID(id=id, db=db, author_id=current_user.id)
    if message.get("error"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message["error"])
    return {"msg": message.get("message")}