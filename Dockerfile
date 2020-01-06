FROM minokun/hadoop_single
MAINTAINER      minukun "952718180@qq.com"

RUN /opt/hadoop-3.1.2/sbin/start-all.sh && \
	/opt/apache-zookeeper-3.5.6-bin/bin/zkServer.sh start && \
	/opt/hbase-1.4.12/bin/start-hbase.sh
RUN echo '' > /opt/hbase-1.4.12/hbase_thrift.log 2>&1
RUN nohup /opt/hbase-1.4.12/bin/hbase thrift start >/opt/hbase-1.4.12/hbase_thrift.log 2>&1 &

EXPOSE 50070
EXPOSE 4040
EXPOSE 2181
EXPOSE 16201
EXPOSE 9000
EXPOSE 9090
