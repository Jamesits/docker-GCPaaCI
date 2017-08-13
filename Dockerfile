FROM alpine:latest
MAINTAINER James Swineson <github@public.swineson.me>

RUN apk --no-cache add python3 py3-pip

WORKDIR /usr/local/src/gcpaaci
COPY . .
RUN pip3 install -r requirements.txt \
    && chmod +x ci.py docker-entrypoint.sh \
    && ln -s /usr/local/src/gcpaaci/docker-entrypoint.sh /usr/local/bin \
    && ln -s /usr/local/src/gcpaaci/ci.py /usr/local/bin/ci

ENTRYPOINT docker-entrypoint.sh
CMD ["ci"]