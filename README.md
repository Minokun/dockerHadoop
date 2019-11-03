# dockerHadoop
## Docker 

dockerhub addr:  https://hub.docker.com/u/minokun

project docker name: minokun/hadoop_single

use tag is v1.1

if you want build it, command： docker pull minokun/hadoop_single:v1.1

docker os is centos8 

all service path under /opt

include follow service

> Hadoop 3.1.2
> Spark 2.4.4
> python 3.7
> Scala 2.12.6

## Log Summary
i put the access.log in hdfs path: /log_file

and summary api data by pyspark

the pyspark program name is log_summary.py

the program ouput the result in hdfs path: /log_summary format csv

## 总结 
我在这里使用了最新的spark和centos，目前为了达到日志分析功能的目的，就先搭建了以上的服务。
使用pyspark来做的本次日式分析。直接过滤出nginx的ip，访问时间，接口，http状态等。
对于分析上，还可以使用ipdb库来解析ip，统计每个城市的访问情况。

在服务上后续还会继续往上增加mysql hive等组件，使整个docker可以直接用来做离线数据分析实验。
但是，总的来说，hadoop的瓶颈大概率在io上，所以生产环境不建议用docker来部署，此次项目只用作实验。

还为日志分析后的docker状态打了一个镜像，可直接使用命令拉取：docker pull minokun/hadoop_single:cerence
log日志名称： access_log hdfs路径：/log_file
输出路径： /log_summary
