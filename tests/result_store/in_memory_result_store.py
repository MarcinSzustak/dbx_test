from pyspark.sql import DataFrame, SparkSession

from example_job.result_store import ResultStore


class InMemoryResultStore(ResultStore):
    def __init__(self, spark: SparkSession):
        self.spark = spark
        self.result = []

    def store(self, dataframe: DataFrame) -> None:
        self.result = dataframe.collect()
