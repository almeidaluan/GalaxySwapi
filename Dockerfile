FROM python:3.6.2rc2
LABEL maintainer "almeida.luan099@gmail.com"
ENV PYTHONUNBUFFERED 1

# creates directory and copies all files
ADD . /GalaxySwapi

# sets work directory
WORKDIR GalaxySwapi

#
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# exposes Flask port
EXPOSE 5000