FROM python:3.8-alpine

ENV PYTHONPATH "/workspace:$PATH"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /workspace

COPY . .

RUN pip3 install -r ./requirements.txt
