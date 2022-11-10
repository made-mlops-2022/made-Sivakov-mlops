import pandas as pd
import logging
import yaml
from marshmallow_dataclass import class_schema
from models.entities.preprocessed_reqs import PreprocessedReqs
from copy import copy

logger = logging.getLogger()


class DataPreprocessing:
    def __init__(self, source_data: pd.DataFrame, hot_encoding_columns: list[str], columns_to_delete: list[str]):
        self.source_data = source_data
        self.hot_encoding_columns = hot_encoding_columns
        self.columns_to_delete = columns_to_delete
        self.final_data = copy(self.source_data)

    def start(self):
        self.del_columns()
        self.one_hot_encoding()

    def del_columns(self):
        self.final_data.drop(columns=self.columns_to_delete, inplace=True)

    def one_hot_encoding(self):
        for column in self.hot_encoding_columns:
            new_df = pd.get_dummies(self.final_data[column], prefix=column)

            for new_column in new_df.columns:
                self.final_data[new_column] = new_df[new_column]

            self.final_data.drop(columns=[column])

    def save(self, path_to_save):
        self.final_data.to_csv(path_to_save)

    def data_normalization(self):
        raise NotImplementedError


if __name__ == '__main__':
    DataPreprocessingSchema = class_schema(PreprocessedReqs)
    logger.info('Start of data preprocessing')

    preproc_conf = ''
    with open(preproc_conf, 'r') as f:
        schema = DataPreprocessingSchema()
        params: PreprocessedReqs = schema.load(yaml.safe_load(f))

    source_data = pd.read_csv(params.source_data_file)
    process = DataPreprocessing(source_data, params.hot_encoding_columns, params.columns_to_delete)
    process.start()

    path_to_save = ''
    process.save(path_to_save)

    logger.info('End of data preprocessing')

