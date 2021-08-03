FROM python:3.9.5

WORKDIR /imageReader-app

RUN pip install mysql-connector-python
RUN pip install webdavclient3

COPY ./app ./app

CMD ["python","./app/main.py"]