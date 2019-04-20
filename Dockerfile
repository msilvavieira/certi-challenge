FROM python:latest
WORKDIR /tornado_server
COPY . /tornado_server

RUN pip install --trusted-host pypi.python.org  -r requirements.txt

EXPOSE 80
CMD ["pytest", "test_int_to_numeral.py"]
