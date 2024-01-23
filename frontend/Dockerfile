FROM python:3.9.5-slim-buster

ADD . ./app

WORKDIR /app

RUN pip3 install -r requirements.txt

# RUN python -m spacy download en_core_web_md

EXPOSE 5004

CMD [ "python","app.py" ]