import sys
import os
import random
from operator import add, mul
from pyspark import SparkContext, SparkConf
from pyspark import SparkFiles
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.types import Row
from pyspark.sql.functions import col,sum

spark = SparkSession.builder.appName("M6-CA1-Instacart-TGA2").getOrCreate() # singleton instance

# hdfs dfs -put orders.csv /user/edureka_672184/use_cases/instacart_csv/
print("\n1. Load Data into Spark DataFrame\n")
aisles_df = spark.read.csv("/user/edureka_672184/use_cases/instacart_csv/aisles.csv", header=True)
department_df = spark.read.csv("/user/edureka_672184/use_cases/instacart_csv/departments.csv", header=True)
products_df = spark.read.csv("/user/edureka_672184/use_cases/instacart_csv/products.csv", header=True)
orders_df = spark.read.csv("/user/edureka_672184/use_cases/instacart_csv/orders.csv", header=True)
orders_products_prior_df = spark.read.csv("/user/edureka_672184/use_cases/instacart_csv/order_products__prior.csv", header=True)
orders_products_train_df = spark.read.csv("/user/edureka_672184/use_cases/instacart_csv/order_products__train.csv", header=True)
#sample_submission_df = spark.read.csv("/user/edureka_672184/use_cases/instacart_csv/sample_submission.csv", header=True)

print("Showing products")
print(products_df.show(5))
print("Showing orders")
print(orders_df.show(5))
print("orders products train")
print(orders_products_train_df.show(5))


print("\n2. Merge all the data frames\n")
prod_dept_aisle = aisles_df \
.join(products_df, on="aisle_id", how='inner') \
.join(department_df, on="department_id", how='inner')


print("products, Department and Aisle combined")
print(prod_dept_aisle.show(5))

print("products, Department and Aisle and other tables combined")

prod_order_prior = orders_df.join(orders_products_prior_df, on="order_id", how='inner')
prod_order_train = orders_df.join(orders_products_train_df, on="order_id", how='inner')
prod_order = prod_order_prior.union(prod_order_train)

instacart_full_df = prod_dept_aisle.join(prod_order, on="product_id", how="inner")

print("Showing 2 rows from the complete dataframe")
instacart_full_df.show(2)

print("showing columns of the complete dataframe")
print(instacart_full_df.columns)

# showing nulls
print("\n3. Check missing data\n")

print("Showing nulls per column ")
print(instacart_full_df.select(*(sum(col(c).isNull().cast("int")).alias(c) for c in instacart_full_df.columns)).show())

print("Days since prior order has 2 million nulls. Other columns are good.")
print("Size of full data is: ", instacart_full_df.count())

print("\n4. List the most ordered products (top 10) \n")
print(instacart_full_df.groupBy(["product_id", "product_name"]).count().orderBy('count', ascending=False).show(10, False))

print("\n5. Do people usually reorder the same previous ordered products? \n")
print(instacart_full_df.groupBy("reordered").count().orderBy('count', ascending=False).show())

print("\n6. List most reordered products \n")
print(instacart_full_df.filter(col("reordered") == 1). \
      groupBy(["product_id", "product_name"]). \
      count().orderBy('count', ascending=False). \
      show(10, False))

print("\n7. Most important department and aisle (by number of products) \n")
print(prod_dept_aisle. \
      groupby(["aisle_id", "aisle", "department_id", "department"]). \
      count().orderBy('count', ascending=False).show(1))

print("\n8. Get the Top 10 departments) \n")
print(prod_dept_aisle. \
      groupby(["department_id", "department"]). \
      count().orderBy('count', ascending=False).show(10, False))

print("\n9. List top 10 products ordered in the morning (6 AM to 11 AM)) \n")
# 6 AM in 24 hour format = 6
# 11 AM in 24 hour format = 11

print(instacart_full_df.filter((col("order_hour_of_day") >= 6) & (col("order_hour_of_day") <= 11)). \
      groupBy(["product_id", "product_name"]). \
      count().orderBy('count', ascending=False).show(10, False))



















