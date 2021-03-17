FROM python:3.8.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /fibonacci

WORKDIR /fibonacci

COPY requirements.txt /fibonacci/

RUN python -m pip install -r requirements.txt

COPY . /fibonacci
