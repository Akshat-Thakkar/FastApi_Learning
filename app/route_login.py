import json
from urllib import response
from fastapi import APIRouter,Request,Depends
from fastapi import responses,status,Form   
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.user import UserCreate
from db.repository.users import create_new_user,get_user_by_email
from pydantic.error_wrappers import ValidationError
from apis.route_login import authenticate_user
from core.security import create_access_token

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()

@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})


@router.post("/register")
def register_user(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    error = []
    try:
        # Check if email already exists
        existing_user = get_user_by_email(email=email, db=db)
        if existing_user:
            error.append("Email: Email already registered")
            return templates.TemplateResponse("auth/register.html", {"request": request, "errors": error})

        user = UserCreate(email=email, password=password)
        create_new_user(db=db, user=user)
        return responses.RedirectResponse("/?alert=successfully%20Registered", status_code=status.HTTP_302_FOUND)
    except ValidationError as e:
        error_list = json.loads(e.json())
        for items in error_list:
            error.append(items.get("loc")[0] + ": " + items.get("msg"))
    return templates.TemplateResponse("auth/register.html", {"request": request, "errors": error})


@router.get("/login")
def login_get(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})

@router.post("/login")
def login_user(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    error=[]
    user = authenticate_user(email=email, password=password, db=db)
    if not user:
        error.append("email: Invalid credentials")
        return templates.TemplateResponse("auth/login.html", {"request": request, "errors": error}, email=email, password=password)
    access_token = create_access_token(data={"sub": user.email})
    response = responses.RedirectResponse("/?alert=successfully%20logged%20in", status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="Authorization", value=f"Bearer {access_token}")
    return response 