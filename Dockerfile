FROM python:3.7.0

ADD . /app

WORKDIR /app

EXPOSE 80/tcp
EXPOSE 80/udp

CMD [ "python", "./app/app.py" ]