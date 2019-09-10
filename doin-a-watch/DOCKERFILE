FROM python:3.7.4-buster
RUN pip install -U pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock /
RUN pipenv install --system
EXPOSE 5001
COPY ./doin-a-watch /app
WORKDIR /app
CMD ["pipenv", "run", "python", "main.py"]