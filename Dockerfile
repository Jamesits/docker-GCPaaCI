FROM alpine:latest
MAINTAINER James Swineson <github@public.swineson.me>

RUN apk --no-cache add python3 py3-pip

WORKDIR /
COPY . .
RUN pip3 install -r requirements.txt \
    && chmod +x ci.py docker-entrypoint.sh \
    && ln -s /ci.py /ci

ENTRYPOINT /docker-entrypoint.sh
CMD ["ci", "-h"]