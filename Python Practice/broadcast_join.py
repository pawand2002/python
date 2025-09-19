from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Initialize a SparkSession
# In a real-world scenario (Databricks, etc.), this is already done for you.
spark = SparkSession.builder.appName("BroadcastJoinDemo").getOrCreate()

# -----------------------------------------------------------
# 1. Create Mock DataFrames to simulate the problem
# -----------------------------------------------------------

# Create a small DataFrame to simulate customer data (fits in memory)
customer_schema = StructType([
    StructField("customer_id", StringType(), True),
    StructField("city", StringType(), True)
])

customer_data = [
    ("cust_1", "New York"),
    ("cust_2", "London"),
    ("cust_3", "Paris"),
    ("cust_4", "Tokyo"),
    ("cust_5", "Sydney")
]
customer_data_df = spark.createDataFrame(data=customer_data, schema=customer_schema)

# Create a large DataFrame to simulate call detail records (CDRs)
# We'll intentionally make one customer_id very common to simulate skew.
cdr_schema = StructType([
    StructField("call_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("call_duration", IntegerType(), True)
])

# Simulate a large amount of data, with many rows for "cust_1"
cdr_data = [
    ("call_001", "cust_1", 120),
    ("call_002", "cust_1", 85),
    ("call_003", "cust_2", 300),
    ("call_004", "cust_1", 60),
    ("call_005", "cust_3", 150),
    ("call_006", "cust_1", 200),
    ("call_007", "cust_4", 90),
    ("call_008", "cust_1", 110),
    ("call_009", "cust_5", 50),
    ("call_010", "cust_1", 75)
]

# We'll expand this list to make the "skew" more obvious
large_cdr_data = cdr_data * 1000  # Simulates a large number of rows
daily_cdr_df = spark.createDataFrame(data=large_cdr_data, schema=cdr_schema)

# -----------------------------------------------------------
# 2. Perform the Broadcast Join
# -----------------------------------------------------------

# Use the broadcast() function on the smaller DataFrame
# This tells Spark to send a copy of customer_data_df to all executors.
# The join happens locally on each executor, preventing data skew.
enriched_cdr_df = daily_cdr_df.join(
    broadcast(customer_data_df),
    on="customer_id",
    how="inner"
)

# -----------------------------------------------------------
# 3. Show the Results
# -----------------------------------------------------------

# This is an action that triggers the execution of the join.
print("Schema after broadcast join:")
enriched_cdr_df.printSchema()

print("Joined DataFrame (first 10 rows):")
enriched_cdr_df.show(10, truncate=False)

# Stop the SparkSession
spark.stop()
