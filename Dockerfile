FROM minokun/hadoop_single
MAINTAINER      minukun "952718180@qq.com"

RUN start-all.sh && \
	zkServer.sh start && \
	start-hbase.sh
RUN echo '' > /opt/hbase-1.4.12/hbase_thrift.log 2>&1
RUN nohup hbase thrift start >/opt/hbase-1.4.12/hbase_thrift.log 2>&1 &

WORKDIR /root
COPY ./access_log ./
COPY ./log_summary.py ./

EXPOSE 50070
EXPOSE 4040
EXPOSE 2181
EXPOSE 16201
EXPOSE 9000
EXPOSE 9090
