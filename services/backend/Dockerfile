FROM python:3.11-buster

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY requirements.txt .
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip --timeout=100 \
    && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt --timeout=100

COPY migrations .
COPY pyproject.toml .

COPY src/ .
COPY setup/ .
