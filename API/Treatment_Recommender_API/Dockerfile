FROM python:3.7-slim-buster
WORKDIR /treatment_API
ENV FLASK_APP=treatment.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5003
COPY . .
RUN ls
CMD ["python3", "treatment.py"]

