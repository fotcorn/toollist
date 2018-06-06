# based on https://www.caktusgroup.com/blog/2017/03/14/production-ready-dockerfile-your-python-django-app/

# builder container with build dependencies
FROM python:3.6-alpine AS builder

ADD ./Pipfile /Pipfile
ADD ./Pipfile.lock /Pipfile.lock

RUN set -ex \
    && apk add --no-cache build-base postgresql-dev linux-headers \
    && pip install pipenv \
    && pipenv install --system --deploy \
    && pip install uwsgi==2.0.17

# create new container without build dependencies
FROM python:3.6-alpine

RUN apk add --no-cache libpq gettext

# copy site-packages with compiled binaries from builder container
COPY --from=builder /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi

# copy code into container
RUN mkdir /code
ADD ./manage.py /code/manage.py
ADD ./toollist/ /code/toollist

ENV DEBUG False
ENV UWSGI_WSGI_FILE=/code/toollist/wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

WORKDIR /code
RUN DATABASE_URL=sqlite:///tmp/db.sqlite SECRET_KEY=none python manage.py collectstatic --noinput
RUN DATABASE_URL=sqlite:///tmp/db.sqlite SECRET_KEY=none python manage.py compilemessages

EXPOSE 8000

CMD ["/usr/local/bin/uwsgi", "--http-auto-chunked", "--http-keepalive"]
