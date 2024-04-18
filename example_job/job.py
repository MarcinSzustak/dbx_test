import argparse
import datetime

from pyspark.sql import SparkSession

from example_job.flow.flow import Flow
from example_job.repository.in_memory_input_repository import InMemoryInputRepository
from example_job.result_store.console_result_store import ConsoleResultStore
from example_job.service import GroupingService


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--date",
        help="Execution Date - format YYYY-MM-DD",
        required=True,
        type=datetime.date.fromisoformat,
    )

    args = parser.parse_known_args()[0]
    execution_date = args.date

    spark = get_spark_session("example-job")

    flow = Flow(
        input_repository=InMemoryInputRepository(spark),
        result_store=ConsoleResultStore(spark),
        grouping_service=GroupingService(),
    )

    flow.execute(execution_date)


def get_spark_session(app_name: str):
    return SparkSession.builder.appName(app_name).getOrCreate()


if __name__ == "__main__":
    main()
