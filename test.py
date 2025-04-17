import os

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from validate import check_for_nulls

spark2 = SparkSession.builder.master("local[*]").appName('hello').getOrCreate()

print(spark2)

df2 = spark2.read.format('csv').option('header', 'True').option('inferSchema', 'True').load(
    'source/oltp/USA_Presc_Medicare_Data_12021.csv')


df_par = spark2.read.format('parquet').load('source/olap/us_cities_dimension.parquet')
#print(df_par.show(5))
#print(df2.show(5))

df_presc = df2.select(df2.npi.alias('presc_id'), df2.nppes_provider_last_org_name.alias('presc_lname'),
                      df2.nppes_provider_first_name.alias('presc_fname'),
                      df2.nppes_provider_city.alias('presc_city'),
                      df2.nppes_provider_state.alias('presc_state'),
                      df2.specialty_description.alias('presc_spclt'),
                      df2.drug_name, df2.total_claim_count.alias('tx_cnt'), df2.total_day_supply,
                      df2.total_drug_cost, df2.years_of_exp)

#print(df_presc.show(5))

df_presc_sel = df_presc.withColumn('Country_name', lit('USA'))


df_presc_sel = df_presc_sel.withColumn('years_of_exp', regexp_replace(col('years_of_exp'), r"^=", " "))

df_presc_sel = df_presc_sel.withColumn('years_of_exp', col('years_of_exp').cast('int'))

        #loggers.warning('concat first and lname ')
df_presc_sel = df_presc_sel.withColumn('presc_fullname', concat_ws(" ", 'presc_lname', 'presc_fname'))

#        loggers.warning("now dropping presc_lname and presc_fname")

df_presc_sel = df_presc_sel.drop('presc_lname', 'presc_fname')

print(df_presc_sel.show(5))

#df_presc_sel = df_presc_sel.select([count(when (isnan(c) | col(c).isNull(), c)).alias(c) for c in df_presc_sel.columns])

#print(df_presc_sel.show())

#df4 = df_presc_sel.filter(col('presc_city').isNull()).count()
#print(df4)


#dfc = check_for_nulls(df_presc_sel, 'df_presc')
#print(dfc.show())
#df_presc_sel = df_presc_sel.dropna(subset="presc_id")
#print(df_presc_sel.show())
#df_presc_sel = df_presc_sel.dropna(subset="drug_name")

#df_presc_sel = df_presc_sel.dropna(subset=['presc_id', 'drug_name'])

#dfc2 = check_for_nulls(df_presc_sel, 'df_presc')
#print(dfc2.show())


mean_avg_tx = df_presc_sel.select(mean(col('tx_cnt'))).collect()[0][0]
print(mean_avg_tx)

print(df_presc_sel.rdd.getNumPartitions())




