FROM python:3.8-alpine
WORKDIR /app

RUN apk add --update --no-cache g++ gcc libxml2-dev libxslt-dev

COPY ./app .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD [ "python", "main.py" ]