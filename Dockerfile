#FROM python:3.7.4-buster
#FROM arm32v6/python:3.7.4-buster
FROM balenalib/raspberrypi4-64-alpine-python
RUN pip install -U pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock /
RUN pipenv install --system
EXPOSE 5001
COPY ./doin-a-watch /app
WORKDIR /app
CMD ["pipenv", "run", "python", "main.py"]