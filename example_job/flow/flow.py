from dataclasses import dataclass
from datetime import date

from example_job.repository import InputRepository
from example_job.result_store import ResultStore
from example_job.service import GroupingService


@dataclass
class Flow:
    input_repository: InputRepository
    result_store: ResultStore
    grouping_service: GroupingService

    def execute(self, execution_date: date) -> None:
        print(f"Executing flow for: {execution_date}")
        input_df = self.input_repository.fetch()
        result = self.grouping_service.aggregate_by_appearance(input_df)
        self.result_store.store(result)
