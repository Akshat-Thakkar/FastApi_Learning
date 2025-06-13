from typing import Optional
from fastapi import APIRouter,Request,Depends   
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.repository.blog import list_blogs , retrieve_blog
from db.session import get_db

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()

@router.get("/")
def home(request: Request, alert: Optional[str] = None, db: Session = Depends(get_db)):
    blogs = list_blogs(db)
    return templates.TemplateResponse("blogs/home.html", {"request": request, "blogs": blogs , "alert": alert})


@router.get("/app/blogs/{id}")
def detail(request: Request, id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    return templates.TemplateResponse("blogs/detail.html", {"request": request, "blog": blog})