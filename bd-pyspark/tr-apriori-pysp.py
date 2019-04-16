from apyori import apriori
from pyspark.sql import SparkSession
import numpy as np 

spark = SparkSession \
		.builder \
		.appName("TRAP") \
		.getOrCreate()

df = spark.read.format("csv").option("header", "false").load("transaction_data.csv")

print(df.count())

association_rules = list(apriori(df.toPandas().values,min_support=0.1, min_confidence=0.2))

for item in association_rules:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print(items)
    # print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")

