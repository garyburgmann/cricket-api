FROM python:3.7.3-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code

RUN pip install -r requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:api", "--reload"]