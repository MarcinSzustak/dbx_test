import pytest
from pyspark.sql import SparkSession

from example_job.job import get_spark_session


@pytest.fixture(scope="session")
def spark_session() -> SparkSession:
    spark = get_spark_session("test-job")
    yield spark
    spark.stop()
