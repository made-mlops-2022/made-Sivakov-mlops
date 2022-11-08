import logging
import time
from datetime import datetime

from models.models_fabric import ModelsFabric
from models.entities.train_params import TrainParams
from marshmallow_dataclass import class_schema
from persistence_manager import PersistenceModelManager
from implemented_models import ImplementedModelsList
from models.entities.preprocessed_data import PreprocessedData
import yaml
import pandas as pd

logger = logging.getLogger()


class TrainProcess:
    def __init__(self, train_params: TrainParams, preprocessed_data: PreprocessedData):
        self.model: ImplementedModelsList = ModelsFabric.create_model(model_type=train_params.model_type,
                                                                      model_params=train_params.model_params)
        self.data = preprocessed_data

    def start_train(self):
        logger.debug('Start train')
        self.model.fit(X=self.data.X, y=self.data.y)
        logger.debug('Model fitted')

    def save_model(self, output_model_file: str):
        PersistenceModelManager.serialize_model_to_file(self.model, output_model_file)
        logger.debug(f'Model saved in {output_model_file}')

    def generate_new_model_name(self):
        return f'{str(self.model)}_{datetime.now()}'


if __name__ == '__main__':
    TrainParamsSchema = class_schema(TrainParams)
    logger.info('Start of train process')

    train_config_file = '../confs/models_confs/random_forest_train_params.yaml'
    with open(train_config_file, 'r') as f:
        schema = TrainParamsSchema()
        params: TrainParams = schema.load(yaml.safe_load(f))

    train_data_file: str = params.train_data_file
    train_data: pd.DataFrame = pd.read_csv(train_data_file)
    preprocessed_data = PreprocessedData(train_data.drop(columns=['condition']), train_data['condition'])

    train_process: TrainProcess = TrainProcess(params, preprocessed_data)
    fitted_model_file: str = params.output_model_file

    train_process.start_train()
    train_process.save_model(fitted_model_file)

    logger.info('End of train process')
