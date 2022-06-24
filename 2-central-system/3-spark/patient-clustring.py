#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install findspark


# In[2]:


import pandas as pd
import numpy as np
from datetime import date, timedelta, datetime
import time
import findspark
findspark.init()


# In[3]:


import pyspark # only run this after findspark.init()
from pyspark.sql import SparkSession, SQLContext
from pyspark.context import SparkContext
from pyspark.sql.functions import * 
from pyspark.sql.types import * 
from pyspark.sql import SparkSession


# # Membuat Data Frame Kondisi Pasien

# In[61]:




spark = SparkSession     .builder     .appName("Patient Condition DataFrame")     .config("spark.some.config.option", "some-value")     .getOrCreate()

#define data schema for file we want to read
patientSchema = StructType([
    StructField("START", StringType(), True),
    StructField("STOP", StringType(), True),
    StructField("PATIENT", StringType(), True),
    StructField("ENCOUNTER", StringType(), True),
    StructField("CODE", StringType(), True),
    StructField("DESCRIPTION", StringType(), True),
])

patientDataframe = spark.read.csv(
    r"C:\Users\My Computer\OneDrive\Documents\TUGAS ABD 4\dataset\conditions.csv", 
    header=True, schema=patientSchema, sep=",")
patientDataframe.show(10)


# # Membuat Subset Data Frame

# In[62]:


patientconditionDataframe = patientDataframe.select(patientDataframe['PATIENT'], 
                                             patientDataframe['DESCRIPTION'])
patientconditionDataframe.show(3);
patientconditionDataframe.printSchema()


# # Explorasi Data Pasien COVID-19

# In[43]:


patientconditionDataframe.filter(patientconditionDataframe.DESCRIPTION=='COVID-19').show()


# # Membuat Dataframe Data Pasien

# In[55]:


spark = SparkSession     .builder     .appName("Patient Clustering")     .config("spark.some.config.option", "some-value")     .getOrCreate()

appName = "Clustering in Spark"
spark = SparkSession     .builder     .appName(appName)     .config("spark.some.config.option", "some-value")     .getOrCreate()

patientInfo = spark.read.csv(
    r"C:\Users\My Computer\OneDrive\Documents\TUGAS ABD 4\dataset\patients.csv", 
    inferSchema=True, header=True)
patientInfo.show()


# # Clustering Data Pasien

# In[56]:


from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler


# In[57]:


assembler = VectorAssembler(inputCols = [
 "STATE", "COUNTY", "GENDER", "RACE", 
    "ETHNICITY"], 
                            outputCol="features")
data = assembler.transform(patientInfo).select('Id', 'features')
data.show(truncate = False, n=3)


# In[58]:


#define kMeans clustering algorithm
kmeans = KMeans(
    featuresCol=assembler.getOutputCol(), 
    predictionCol="cluster", k=5)
model = kmeans.fit(data)
print ("Model is successfully trained!")


# In[59]:


centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)


# In[60]:


prediction = model.transform(data)#cluster given data
prediction.groupBy("cluster").count().orderBy("cluster").show()#count members in each cluster
prediction.select('Id', 'cluster').show(5)#show several clustered data


# In[ ]:




