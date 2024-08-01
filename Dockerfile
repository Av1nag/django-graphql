FROM python:3.12.4-alpine3.19

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app

RUN python -m venv /.venv && \
    /.venv/bin/pip install --upgrade pip && \
    /.venv/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app

ENV PATH="/.venv/bin:$PATH"
USER app