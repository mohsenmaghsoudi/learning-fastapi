from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None  +ptyhon < 3.10
    rating: int | None = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.title)
    print(new_post.content)
    print(new_post.published)
    print(new_post.rating)
    print(new_post.model_dump())  # convert to dictionary
    return {"data": new_post}
