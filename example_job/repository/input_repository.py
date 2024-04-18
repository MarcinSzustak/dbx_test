from abc import ABC, abstractmethod

from pyspark.sql import DataFrame


class InputRepository(ABC):
    @abstractmethod
    def fetch(self) -> DataFrame:
        raise NotImplementedError()
