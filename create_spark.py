from pyspark.sql import SparkSession
import sys

import logging.config

logging.config.fileConfig('Properties/configuration/logging.config')

logger = logging.getLogger('Create_spark')

def get_spark_object(envn, appName):
    try:
        logger.info('get_spark_object method started')

        if envn == 'DEV':
            master = 'local'

        else:
            master = 'Yarn'

        logger.info('master is {}'.format(master))

        spark = SparkSession.builder \
                            .master(master) \
                            .appName(appName) \
                            .enableHiveSupport() \
                            .config("spark.driver.extraClassPath", "mysql-connector-java-8.0.29.jar") \
                            .getOrCreate()
                            
        # Python version
        print("Python Version:", sys.version)

        # Spark version
        print("Spark Version:", spark.version)

        # Java version
        print("Java Version:", spark._jvm.java.lang.System.getProperty("java.version"))

        # Hadoop version
        print("Hadoop Version:", spark._jvm.org.apache.hadoop.util.VersionInfo.getVersion())

    except Exception as exp:
        logger.error('An error occurred in the get_spark_object==== ', str(exp))
        raise

    else:
        logger.info('Spark object created.....')
    return spark

# get_spark_object("DEV", "pyspark-app")