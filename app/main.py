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

import time
from random import randrange

import psycopg
from fastapi import FastAPI, HTTPException, Response, status
from psycopg import rows
from pydantic import BaseModel

app = FastAPI()

DB_URL = "postgresql://admin:admin@localhost:5432/fastapi"

while True:
    try:
        # conn = psycopg.connect(
        #     DB_URL,
        #     row_factory=rows.dict_row,
        # )
        conn = psycopg.connect(
            host="localhost",
            port=5432,
            dbname="fastapi",
            user="admin",
            password="admin",
            row_factory=rows.dict_row,
        )
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error :", error)
        time.sleep(5)


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
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    # post_id = randrange(0, 100000)
    # print(post)
    # print(post.model_dump())
    cursor.execute(
        """ INSERT INTO posts (title, content, published) VALUES (%s,%s,%s) RETURNING * """,
        (post.title, post.content, post.published),
    )
    new_post = cursor.fetchone()
    conn.commit()

    return {"post_detail": new_post}


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
    if post_index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found.",
        )

    my_posts.pop(post_index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):

    post_index = fint_post_index(id)
    if post_index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found.",
        )
    post_dict = post.model_dump()
    post_dict["id"] = id
    my_posts[post_index] = post_dict
    return {"message": post_dict}
