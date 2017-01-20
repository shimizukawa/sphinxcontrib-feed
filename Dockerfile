FROM python:3.5.2

COPY . /app
RUN pip install -r /app/test-requirements.txt /app/

CMD pytest /app/tests

