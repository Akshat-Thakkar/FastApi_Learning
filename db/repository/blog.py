from sqlalchemy.orm import Session
from schemas.blog import CreateBlog ,UpdateBlog
from db.models.blog import Blog

def create_new_blog(blog: CreateBlog, db: Session, author_id: int):
   blog = Blog(
      title=blog.title,
      slug=blog.slug,
      content=blog.content,
      author_id=author_id
   )
   db.add(blog)
   db.commit()
   db.refresh(blog)
   return blog



def retrieve_blog(id: int , db: Session ) :
    blog =db.query(Blog).filter(Blog.id == id).first()
    return  blog

def retrieve_active_blog(db: Session):
    return db.query(Blog).filter(Blog.is_active == True).all()

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
    db.delete(blog)
    db.commit()
    return {"message": f"Blog with ID {id} deleted successfully"}
