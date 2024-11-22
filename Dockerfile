FROM python:3.12-slim-bookworm

LABEL maintainer="Cameron Rosier <rosiercam@gmail.com>"

WORKDIR /opt/robopd2-api
COPY ./src requirements.txt ./

RUN apt -y update \
    && apt install -y gcc \
    && python -m pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]