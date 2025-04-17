import os

os.environ['envn'] = 'DEV'
os.environ['header'] = 'True'
os.environ['inferSchema'] = 'True'
os.environ['user'] = 'root'
os.environ['password'] = '9110580222'

header = os.environ['header']
inferSchema = os.environ['inferSchema']
envn = os.environ['envn']

user = os.environ['user']
password = os.environ['password']

appName = 'pyspark-app'

current = os.getcwd()

src_olap = current + '\source\olap'

src_oltp = current + '\source\oltp'

city_path = 'output\cities'

presc_path = 'output\prescriber'

os.environ["HADOOP_HOME"] = "C:\\spark\\hadoop"
os.environ["PATH"] += os.pathsep + os.path.join(os.environ["HADOOP_HOME"], "bin")
