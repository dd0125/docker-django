FROM ubuntu:18.04

# 地域言語設定
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
# ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9

# 特定のパッケージインストール時に地域を聞かれないようにする
ENV DEBIAN_FRONTEND=noninteractive

# apt の更新
RUN apt -y update
# RUN apt -y upgrade


# python のインストール
RUN apt install -y build-essential libbz2-dev libdb-dev \
  libreadline-dev libffi-dev libgdbm-dev liblzma-dev \
  libncursesw5-dev libsqlite3-dev libssl-dev \
  zlib1g-dev uuid-dev tk-dev

RUN apt install -y python3.7

RUN python3.7 --version



# pip のインストール
RUN apt install -y python3-pip
RUN pip3 install --upgrade pip

# django のインストール
RUN pip3 install django
RUN apt install -y python-django-common
RUN django-admin --version


# uwsgi のインストール
RUN pip3 install uwsgi

# uwsgi の起動
CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
# CMD ["uwsgi" ,"--http" ,":8000" ,"--wsgi-file" ,"/var/www/sample/sample/test.py"]
# CMD ["uwsgi" ,"--http" ,":8000" ,"--file" ,"/var/www/sample/sample/wsgi.py"]

# django server の起動
# WORKDIR /var/www/sample
# RUN pwd
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]