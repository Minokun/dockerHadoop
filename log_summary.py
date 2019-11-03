from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.functions import udf
from pyspark.sql import functions as f
from pyspark.sql.types import *

if __name__ == '__main__':
    conf = SparkConf().setAppName('nginx日志接口统计分析')
    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    # 读取hdfs上的日志文件
    acc_log_df = spark.read.text("hdfs://localhost:8020/log_file/access_log")
    acc_log_df.cache()

    # 查找每一条访问记录的ip 空格分隔 第1个是ip 第4个是时间 第6个是接口访问方式
    def getIp(line):
        return line.split(' ')[0]

    def getTime(line):
        return line.split(' ')[3].replace('[', '')

    def getAPIType(line):
        return line.split(' ')[5].replace('"', '')

    # 注册自定义函数
    get_ip = udf(getIp, StringType())
    get_time = udf(getTime, StringType())
    get_api_type = udf(getAPIType, StringType())

    # 获取新的列
    df1 = acc_log_df.withColumn('ip', get_ip(acc_log_df['value'])).\
        withColumn('time', get_time(acc_log_df['value'])).\
        withColumn('api_type', get_api_type(acc_log_df['value']))

    # 去掉api_type 为 - 的记录
    df2 = df1.filter(df1.api_type != '-')

    # 获取访问接口名称 用api_type 分隔后数据第二个元素 至 第一个字符'"'便是
    def getAPIName(value, api_type):
        try:
            deal = value.split(api_type)[1]
            res = deal[1:deal.index('"')].split(' ')[0]
        except Exception as e:
            res = ''
        return res

    # 获取 http type
    def getHttpType(value, api_type):
        try:
            deal = value.split(api_type)[1]
            res = deal[1:deal.index('"')].split(' ')[1]
        except Exception as e:
            res = ''
        return res

    # 获取http code 用http_type 分隔 第二个元素 用' ' 分隔的第二元素便是
    def getHttpCode(value, http_type):
        try:
            res = value.split(http_type)[1].split(' ')[1]
        except Exception as e:
            res = ''
        return res

    get_api_name = udf(getAPIName, StringType())
    get_http_type = udf(getHttpType, StringType())
    get_http_code = udf(getHttpCode, StringType())

    df3 = df2.withColumn("api_name", get_api_name(df2['value'], df2['api_type'])).\
        withColumn("http_type", get_http_type(df2['value'], df2['api_type']))

    df4 = df3.withColumn('http_code', get_http_code(df3['value'], df3['http_type']))

    # 接下来即可统计ip,时间分布，接口，返回情况数据，还可以利用ipdb将ip转换成城市统计个城市访问情况
    # 此处只统计接口访问情况 并输入至hdfs
    df5 = df4.groupBy('api_name').count()
    res_df = df5.orderBy(df5['count'].desc())
    res_df.write.csv("hdfs://localhost:8020/log_summary/api_summary.csv")