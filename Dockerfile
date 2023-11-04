FROM python:3.9.18-bullseye

COPY . .

RUN pip install requests
ENV LIST ./raw_url

CMD python /script.py