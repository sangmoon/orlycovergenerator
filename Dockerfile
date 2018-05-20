FROM askdjango/django_base:0.3
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi

RUN mkdir /djproj
WORKDIR /djproj
ADD . /djproj/
RUN pip3 install -r reqs/prod.txt

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE covergenerator.settings.prod

EXPOSE 8080
USER uwsgi

CMD ["uwsgi", "--http", "0.0.0.0:8080", "--wsgi-file", "/djproj/covergenerator/wsgi.py"]