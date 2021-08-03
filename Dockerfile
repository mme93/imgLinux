FROM python:3.9.5

WORKDIR /imageReader-app

COPY ./app ./app

CMD ["python","./app/main.py"]