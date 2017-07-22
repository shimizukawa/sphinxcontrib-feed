FROM python:3.6.1

COPY . /app
RUN pip install -r /app/test-requirements.txt
RUN pip install -e /app/

CMD pytest /app/tests

