FROM python:3.6.4
MAINTAINER Michael Henry Pantaleon

ENV PROJECT_PATH /home
WORKDIR $PROJECT_PATH

COPY requirements.txt $PROJECT_PATH
RUN pip install -r requirements.txt
COPY . $PROJECT_PATH

ENV DJANGO_SETTINGS_MODULE project.settings.production
ENV PORT 8001

EXPOSE $PORT
ENTRYPOINT sh entrypoint-docker.sh