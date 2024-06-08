from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
from pyspark.sql.window import Window
from pyspark.sql.functions import lag
from pyspark.sql.functions import col
from pyspark.sql.functions import when

def process_data(input_path, output_path):
    spark = SparkSession.builder \
        .appName("FinancialDataProcessingApp") \
        .getOrCreate()

    # Read data
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    # Example transformation: Calculate moving average of a column
    window_spec = Window.orderBy("date").rowsBetween(-3, 0)
    result_df = df.withColumn("moving_avg", avg(col("value")).over(window_spec))

    # Add a lag column to simulate forecasting
    result_df = result_df.withColumn("lag_value", lag("value", 1).over(Window.orderBy("date")))
    result_df = result_df.withColumn("forecast", when(col("lag_value").isNull(), col("value")).otherwise(col("lag_value")))

    # Write the result to a CSV file
    result_df.write.csv(output_path, header=True)

    spark.stop()

if __name__ == "__main__":
    input_path = "data/input_data.csv"
    output_path = "data/processed_data"
    process_data(input_path, output_path)
