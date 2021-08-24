FROM python:3.7-slim-buster
WORKDIR /treatement_API
ENV FLASK_APP=treatement.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5003
COPY . .
RUN ls
CMD ["python3", "treatement.py"]
