from datetime import date

from pyspark import Row
from pyspark.sql import SparkSession

from example_job.flow.flow import Flow
from example_job.repository.in_memory_input_repository import InMemoryInputRepository
from example_job.service import GroupingService
from tests.result_store import InMemoryResultStore


def test_flow(spark_session: SparkSession):
    input_repository = InMemoryInputRepository(spark_session)
    result_store = InMemoryResultStore(spark_session)
    grouping_service = GroupingService()
    flow = Flow(
        input_repository=input_repository,
        result_store=result_store,
        grouping_service=grouping_service,
    )

    expected_result = [
        Row(character="Ezio", appearance=3),
        Row(character="Altair", appearance=1),
        Row(character="Connor", appearance=1),
    ]

    flow.execute(execution_date=date(2022, 11, 3))

    assert result_store.result == expected_result
