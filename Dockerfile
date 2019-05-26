FROM python:3.7.3-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "server:api", "--reload"]
CMD alembic upgrade head && gunicorn -w 4 -b 0.0.0.0:8000 server:api --reload