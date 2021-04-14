FROM python:3.9.4-slim-buster

LABEL maintainer="Daniel Orozco <danor.dcor@gmail.com>"

RUN mkdir -p /usr/src/app
ENV PYTHONPATH=$PYTHONPATH:/usr/src/app
ENV PYTHONPATH=/usr/src/app/src:$PYTHONPATH
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy static attrs (non dev) to /usr/app/
COPY app/ app/
EXPOSE 8000