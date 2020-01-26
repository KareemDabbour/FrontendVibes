FROM python:3.7

##############
### Config ###
##############
ENV APP_PATH=/player
ENV APP_USER=player
ARG UID
ARG GID

# Create app user
RUN groupadd --g $GID $APP_USER || true
RUN useradd --uid $UID --gid $GID --system --no-create-home --home-dir $APP_PATH $APP_USER || true

RUN mkdir $APP_PATH

WORKDIR $APP_PATH

COPY requirements.txt /tmp

RUN pip3 install -r /tmp/requirements.txt

RUN apt-get update && apt-get install -y alsa-utils

COPY . $APP_PATH

CMD ["./bin/start-server"]
