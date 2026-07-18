from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.title)
    print(new_post.content)
    return {"data": "new post"}
