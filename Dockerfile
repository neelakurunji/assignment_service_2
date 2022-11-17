FROM ubuntu:20.04

RUN apt-get update && apt-get install -y wget git unzip make uvicorn python3-pip

COPY . /opt/service

RUN python3 -m pip install fastapi pymongo

CMD ["uvicorn", "main:app", "--port=8900"]

EXPOSE 8900