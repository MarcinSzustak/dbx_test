from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import StructType, StructField, StringType

from example_job.repository import InputRepository


class InMemoryInputRepository(InputRepository):
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def fetch(self) -> DataFrame:
        input_data = [
            ("Assassin's Creed", "Altair"),
            ("Assassin's Creed II", "Ezio"),
            ("Assassin's Creed Brotherhood", "Ezio"),
            ("Assassin's Creed Revelation", "Ezio"),
            ("Assassin's Creed III", "Connor"),
        ]
        schema = StructType(
            [
                StructField(name="game", dataType=StringType(), nullable=False),
                StructField(name="character", dataType=StringType(), nullable=False),
            ]
        )
        return self.spark.createDataFrame(data=input_data, schema=schema)
