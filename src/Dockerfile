FROM tiangolo/uvicorn-gunicorn:python3.12

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt  /usr/src/requirements.txt
RUN set -eux \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/requirements.txt \
    && rm -rf /root/.cache/pip

#copy project
COPY . /usr/src/app
