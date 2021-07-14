FROM python:3.7.1

RUN set -ex && mkdir /app
RUN pip3 install pipenv

WORKDIR /app

EXPOSE 1115

COPY . /app/
RUN pipenv run pip install -r requirements.txt

CMD pipenv run python main.py