FROM python:3.7.0

ADD . /app

WORKDIR /app

EXPOSE 5000
CMD [ "python", "./app/app.py" ]