FROM python:3.9-slim
WORKDIR /usr/src/app
RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
