import pyspark.sql.functions as F
from pyspark.sql import DataFrame


class GroupingService:
    appearance_column_name = "appearance"

    def aggregate_by_appearance(self, ac_character: DataFrame) -> DataFrame:
        return (
            ac_character.groupBy("character")
            .agg(F.count("*").alias(self.appearance_column_name))
            .orderBy(F.col(self.appearance_column_name).desc(), F.col("character"))
        )
