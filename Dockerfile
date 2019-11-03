FROM minokun/hadoop_single:v1.1
MAINTAINER      minukun "952718180@qq.com"

COPY ./access_log /opt/
COPY ./log_summary.py /opt/
RUN source/etc/profile
RUN hadoop fs -mkdir /log_file
RUN hadoop fs -mkdir /log_summary
RUN hadoop fs -put /opt/access_log /log_file/
RUN spark-submit --master yarn ./log_summary.py

