from dataclasses import dataclass


@dataclass()
class PreprocessedReqs:
    source_data_file: str
    columns_to_delete: list[str]
    hot_encoding_columns: list[str]
