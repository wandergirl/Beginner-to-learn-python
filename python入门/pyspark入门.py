"""
            安装pysprk 第三方包使用pyspark 在命令窗口使用 pip install pyspark命令安装spark
            想要使用pyspark完成数据处理首先需要构建一个执行环境入口对象
            spark的执行环境入口对象是: SparkContext 的类对象

"""
# 导入pyspark包
# from pyspark import SparkConf ,SparkContext
#
# # 创建SparkConf类对象
# conf = SparkConf().setMaster("local[*]").setAppName("pyspark")
#
# sc = SparkContext(conf = conf)
# print(sc.version)
# sc.stop()

from pyspark import SparkContext
logFile = "file:////usr/local/hadoop-2.8.5/README.txt"
sc = SparkContext("local", "Hello PySpark")
logData = sc.textFile(logFile).cache()
numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
print("Line with a:%i,lines with b :%i" % (numAs, numBs))