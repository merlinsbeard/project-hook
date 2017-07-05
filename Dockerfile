FROM python:3.6.1

ADD . /hooker
COPY ./entrypoint /hooker/
WORKDIR /hooker
RUN pip install --no-cache-dir -r requirements.txt
EXOPOSE 8000
ENV DJANGO_SETTINGS_MODULE config.settings.local
RUN ["chmod", "+x", "/hooker/entrypoint.sh"]
