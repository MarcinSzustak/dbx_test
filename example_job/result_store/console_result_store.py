from pyspark.sql import DataFrame, SparkSession

from example_job.result_store import ResultStore


class ConsoleResultStore(ResultStore):
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def store(self, dataframe: DataFrame) -> None:
        print("Assassin's Creed characters with the most appearance in franchise:")
        dataframe.show()
