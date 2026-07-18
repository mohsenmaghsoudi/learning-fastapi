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


# priority of path param, pydantic param, query param

# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# # مدل Pydantic
# class Book(BaseModel):
#     title: str
#     author: str
#     rating: int
#
# @app.put("/books/{book_id}")
# async def update_book(
#     book_id: int,          # 1. Path Parameter (اجباری - بدون پیش‌فرض)
#     book_data: Book,       # 2. Pydantic Model (اجباری - بدون پیش‌فرض)
#     q: str | None = None   # 3. Query Parameter (اختیاری - با پیش‌فرض None)
# ):
#     result = {"book_id": book_id, **book_data.model_dump()}
#
#     if q:
#         result.update({"q": q})
#
