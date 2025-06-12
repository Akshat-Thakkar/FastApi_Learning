from typing import Optional
from pydantic import BaseModel,root_validator
from datetime import datetime

class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None
    published: bool = True
    created_at: datetime = datetime.now()

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if not values.get("slug"):
            values["slug"] = values.get("title", "").replace(" ", "-").lower()
        return values


class ShowBlog(BaseModel):
    title: str
    content: Optional[str] = None
    created_at: datetime = datetime.now()

    class Config:
        orm_mode = True