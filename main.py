import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    binary: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/image/{binary}")
def read_item(binary: str, param: str = None):
    print(binary)
    return {"binary": binary, "param": param}


@app.post("/image_post")
def post_hello(image: Image):
    print(image.binary)
    return image


if __name__ == '__main__':
    uvicorn.run(app)
