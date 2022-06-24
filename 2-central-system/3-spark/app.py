import pyspark
from kafka import KafkaConsumer, KafkaProducer
from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder.appName('app').getOrCreate()

consumer = KafkaConsumer('gateway-spark')
for message in consumer:
        df = spark.read.json(message)
        df = spark.createDataFrame(rawData, schema=mySchema)
        countMale =  df.filter(df["Gender"] != "male")
        countFemale =  df.filter(df["Gender"] != "female")

        producer = KafkaProducer(bootstrap_servers="localhost:9092")
        producer.send('spark-fhir', {
            data: df,
            countMale: countMale,
            countFemale: countFemale,
        })


