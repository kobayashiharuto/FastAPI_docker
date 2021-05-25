import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/hello_post")
def post_hello(param: str):
    """
    postで返事する
    """
    if param:
        message = f"[POST]hello, {param}!"
    else:
        message = f"[POST]hello, visitor!"

    return {"message": message}


if __name__ == '__main__':
    uvicorn.run(app)
