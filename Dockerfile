FROM ubuntu:14.04
MAINTAINER Clint Liddick <cliddick@andrew.cmu.edu>

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -qq && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libxml2-dev \
    libxslt1-dev \
    python-dev \
    zlib1g-dev

RUN curl -Lk https://bootstrap.pypa.io/get-pip.py | python
RUN pip install uwsgi==2.0.11.1

COPY server/requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir -p /var/www

COPY server  /var/www/server
COPY Snap    /var/www/Snap

WORKDIR /var/www
RUN chown -R www-data server Snap

# default Flask port
EXPOSE 5000

USER www-data
WORKDIR /var/www/server
CMD ["/usr/local/bin/uwsgi", "--socket", ":5000", "--wsgi-file", "flask_server.py", "--callable", "app", "--master"]
