FROM python:2.7.11

COPY . /app
RUN pip install -r /app/test-requirements.txt /app/

CMD pytest /app/tests

