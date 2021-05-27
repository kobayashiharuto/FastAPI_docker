import os
from tensorflow import keras
import numpy as np
import distutils.util
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# strサイズ 28*28
IMAGE_STR_MOCK = '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000111111100000000000000000001100000011111000000000000000100000000000110000000000000010000000000001110000000000001000111000000001100000000000100010100000000011000000000010001110000000000110000000011000000000000000001100000001000000000000000000011000000010000000000000000000100000001100000000000000000010000000011000000000000000011000000000100000000000000011000000000001000000000000001000000000000110000000000001100000000000001100000000011000000000000000011000000011000000000000000000110000011000000000000000000001110110000000000000000000000001110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
MODEL = keras.models.load_model('app/model1_1.h5')


def predict(image_str: str):
    image_model = ApiImageModel(28)
    image = image_model.decode_image(image_str)
    image = np.expand_dims(image, 0)

    print(os.path.exists('app/model1_1.h5'))
    # 学習済みモデルを読み込む

    # 予想開始
    predictions = MODEL.predict(image)
    predictions = predictions.reshape(-1)
    print(f'PREDICT: {np.argmax(predictions)}')
    maxIndex = predictions.argsort()[-5:][::-1]
    print(maxIndex)

    return ','.join(list(map(str, maxIndex.tolist())))


class ApiImageModel():
    def __init__(self, image_size):
        self._image_size = image_size

    # strをuint8の2次元配列にデコード
    def decode_image(self, image_str):
        image = np.array([[bool(distutils.util.strtobool(
            image_str[i + self._image_size * j])) for i in range(self._image_size)] for j in range(self._image_size)], dtype='u8')
        return image


class Image(BaseModel):
    binary: str


@app.get("/")
def read_root():
    return {"Hello!!!": "Worlds"}


@app.get("/image/{binary}")
def read_item(binary: str, param: str = None):
    print(binary)
    data = predict(IMAGE_STR_MOCK)
    return {"binary": binary, "param": param, "predict": data}


@app.post("/image_post")
def post_hello(image: Image):
    print(image.binary)
    return image


if __name__ == '__main__':
    uvicorn.run(app)
