FROM python:3.9.5

WORKDIR /imageReader-app

RUN pip install Pillow
RUN pip install numpy


COPY ./app ./app

CMD ["python","./app/main.py"]