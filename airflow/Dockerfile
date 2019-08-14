FROM debian:latest
MAINTAINER pmotwani575@gmail.com
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y \
    python \
    python-setuptools \
    python-pip

COPY ./requirements1.txt /requirements1.txt

RUN pip install -r requirements1.txt
RUN pip install requests
RUN pip install apache-airflow
RUN pip install apache-airflow[postgres]
RUN airflow initdb
ADD ./airflow.sh /usr/local/bin/airflow.sh
RUN chmod +x /usr/local/bin/airflow.sh
#ADD ./dags.py /usr/local/bin/dags.py
#RUN chmod +x /usr/local/bin/dags.py
#ENTRYPOINT ["dags.py"]


EXPOSE 8080

ENTRYPOINT ["airflow.sh"]
