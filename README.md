# dockerHadoop
## Docker 

dockerhub addr:  https://hub.docker.com/u/minokun

project docker name: minokun/hadoop_single

use tag is latest

the zookeeper hbase download url:
http://mirrors.tuna.tsinghua.edu.cn/apache/hbase/hbase-1.4.12/hbase-1.4.12-bin.tar.gz
http://mirror.bit.edu.cn/apache/zookeeper/stable/apache-zookeeper-3.5.6-bin.tar.gz

docker os is centos8 

all service path under /opt

include follow service

> Hadoop 3.1.2
> Spark 2.4.4
> python 3.7
> Scala 2.12.6
> Hbase1.4.12
> Zookeeper3.5.6

```shell
# run contains
docker run -itd --name hadoop -p 8001:50070 -p 8002:60010 -p 8003:4040 -p 2181:2181 -p 16201:16201 -p 9000:9000 -p 9020:9020 minokun/hadoop_single
# start hadoop
start-all.sh
# start zookeeper
zkServer.sh start
# start hbase
start-hbase.sh
# start hbase thrift
echo '' > /opt/hbase-1.4.12/hbase_thrift.log
nohup /opt/hbase-1.4.12/bin/hbase thrift start >/opt/hbase-1.4.12/hbase
