import logging.config
import platform

from pyspark.sql.functions import *
from pyspark.sql.types import *

logging.config.fileConfig('Properties/configuration/logging.config')
loggers = logging.getLogger('Extraction')

def extract_files(df, format, filepath, split_no, headerReq, compressionType):
    try:
        loggers.warning("extract_files method started executing....")
        
        print("filepath= {}".format(filepath))
        
        # split_no is number of split files..
        #df.coalesce(split_no).write.mode("overwrite").format(format).save(filepath, header=headerReq,compression=compressionType)
        
        df.coalesce(split_no).write \
        .format("csv") \
        .option("header", headerReq) \
        .option("compression", compressionType) \
        .save(filepath)

        # # Prepare the writer
        # writer = df.coalesce(split_no).write \
        #     .mode("overwrite") \
        #     .format(format) \
        #     .option("compression", compressionType)

        # # No header option for ORC or Parquet
        # writer.save(filepath)
        
    except Exception as e:
        loggers.error("An error occured at extract_files method:::::", str(e))

        raise

    else:
        loggers.warning("extract_file method successfully executed...")
