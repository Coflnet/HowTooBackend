FROM python:3.10

WORKDIR /
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY . /
RUN uvicorn src.main:app --reload --host 0.0.0.0 --port 8000