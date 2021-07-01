FROM python:3.7-slim-buster
WORKDIR /Image_Classification_API
ENV FLASK_APP=image_classification_API.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5001
COPY . .
CMD ["python3", "image_classification_API.py"]
