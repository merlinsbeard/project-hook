FROM python:3.6.1

ADD . /hooker
COPY ./entrypoint.sh /hooker/
WORKDIR /hooker
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE config.settings.prod
RUN ["chmod", "+x", "/hooker/entrypoint.sh"]
ENTRYPOINT ["sh","/hooker/entrypoint.sh"]
