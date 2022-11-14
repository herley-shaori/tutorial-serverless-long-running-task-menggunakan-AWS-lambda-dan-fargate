FROM public.ecr.aws/docker/library/python:3.8.15-alpine3.16
COPY main.py .
COPY requirements.txt .
COPY config /root/.aws/config
COPY credentials /root/.aws/credentials
RUN pip install -r requirements.txt
ENTRYPOINT python main.py --random-string ${RANDOM_STRING_FROM_LAMBDA}