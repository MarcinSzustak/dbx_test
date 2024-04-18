from abc import ABC, abstractmethod

from pyspark.sql import DataFrame


class ResultStore(ABC):
    @abstractmethod
    def store(self, dataframe: DataFrame) -> None:
        raise NotImplementedError()
