FROM python:3.7

RUN pip install fastapi uvicorn tensorflow --no-cache-dir

EXPOSE 80