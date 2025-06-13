from sqlalchemy.orm import Session
from schemas.blog import CreateBlog ,UpdateBlog
from db.models.blog import Blog

def create_new_blog(blog: CreateBlog, db: Session, author_id: int):
   blog = Blog(
      title=blog.title,
      slug=blog.slug,
      content=blog.content,
      author_id=author_id,
      isActive=blog.isActive
   )
   db.add(blog)
   db.commit()
   db.refresh(blog)
   return blog

def list_blogs(db: Session):
    blogs = db.query(Blog).all()
    return blogs

def retrieve_blog(id: int , db: Session ) :
    blog =db.query(Blog).filter(Blog.id == id).first()
    return  blog


def update_blog_by_id(id: int, blog: UpdateBlog, db: Session, author_id: int = 1):
    existing_blog = db.query(Blog).filter(Blog.id == id).first()
    if not existing_blog:
        return
    existing_blog.title = blog.title
    existing_blog.content = blog.content
    db.add(existing_blog)
    db.commit()
    return existing_blog

def delete_blog_by_ID(id: int, db: Session, author_id: int = 1):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        return {"error ": f"Blog with ID {id} not found"}
    if blog.author_id != author_id:
        return {"error": "You do not have permission to delete this blog"}
    db.delete(blog)
    db.commit()
    return {"message": f"Blog with ID {id} deleted successfully"}
