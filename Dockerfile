FROM python:3.7

RUN pip install fastapi uvicorn tensorflow

EXPOSE 80