FROM python:3.7

RUN pip install pipenv

WORKDIR /opt/the-coffee-bar

COPY src ./src
COPY Pipfile setup.py README.md ./

RUN pipenv lock --pre
RUN pipenv install --system
