FROM python:3.9.5

WORKDIR /imageReader-app

RUN pip install Pillow
RUN pip install numpy
RUN pip install python3-opencv

COPY ./app ./app

CMD ["python","./app/main.py"]