FROM python:latest
WORKDIR ./project
COPY . /project
RUN pip install -r requirements.txt
RUN ["python", "manage.py", "makemigrations"]

EXPOSE 8000