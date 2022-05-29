FROM alpine:latest

COPY . .

RUN apk add curl git python3 && curl https://get.okteto.com -sSfL | sh

CMD ["python3", "okteto-up.py"]
© 2022 GitHub, Inc.
Terms
Privacy
