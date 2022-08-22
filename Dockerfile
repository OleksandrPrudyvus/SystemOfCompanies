# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/dp_rest

COPY requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt
COPY . /usr/src/dp_rest

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]