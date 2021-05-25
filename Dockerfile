FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /fastapi_app

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload"]


