# @app.post("/createposts")
# def create_posts(new_post: Post):
#     print(new_post)
#     print(new_post.title)
#     print(new_post.content)
#     print(new_post.published)
#     print(new_post.rating)
#     print(new_post.model_dump())  # convert to dictionary
#     return {"data": new_post}


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

from random import randrange

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None  +ptyhon < 3.10
    rating: int | None = None


my_posts = [
    {"title": "title of post 1", "content": "content of post1", "id": 1},
    {"title": "title of post 2", "content": "content of post 2", "id": 2},
]


def find_post(id: int):
    for post in my_posts:
        if post["id"] == id:
            return post


def fint_post_index(id: int):
    for index, post in enumerate(my_posts):
        if post["id"] == id:
            return index


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_id = randrange(0, 100000)
    # print(post)
    # print(post.model_dump())
    my_posts.append({**post.model_dump(), "id": post_id})
    return {"post_detail": post}


# @app.get("/posts/latest")
# def get_latest_post():
#     return my_posts[-1]


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found."}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found.",
        )

    return {"data": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post_index = fint_post_index(id)
    if not post_index:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found.",
        )

    my_posts.pop(post_index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
