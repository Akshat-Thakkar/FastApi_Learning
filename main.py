from fastapi import FastAPI

app = FastAPI(title="My FastAPI Application",version="0.1.0")

@app.get("/")
def hello():
    return {"Hello": "fastapi"}