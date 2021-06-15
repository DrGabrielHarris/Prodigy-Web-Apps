# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

FROM python:3.7

COPY requirements.txt /app/
WORKDIR /app

RUN pip install --upgrade pip \
    && pip install --trusted-host pypi.python.org -r requirements.txt

COPY wheel/prodigy-xxx-linux_x86_64.whl ./wheel/
RUN pip install wheel/prodigy-xxx-linux_x86_64.whl \
    && rm -rf wheel/prodigy-xxx-linux_x86_64.whl
RUN python -m spacy download en_core_web_md

COPY prodigy.json .
COPY data ./data/

ENV PRODIGY_HOME /app
ENV PRODIGY_LOGGING "verbose"
ENV PRODIGY_ALLOWED_SESSIONS "user1,user2"
ENV PRODIGY_BASIC_AUTH_USER "admin"
ENV PRODIGY_BASIC_AUTH_PASS "password"

EXPOSE 80

CMD python -m prodigy ner.manual ner_news en_core_web_md ./data/dataset.jsonl --label PERSON,ORG,PRODUCT