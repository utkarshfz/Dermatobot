



FROM python:3.7-slim-buster
WORKDIR /Symptoms_Classification_API
ENV FLASK_APP=symptoms_classification_api.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5002
COPY . .
CMD ["python3", "symptoms_classification_api.py"]
