import logging
import os.path

import yaml
import pandas as pd
from marshmallow_dataclass import class_schema
from ml_project.models.entities.prediction_params import PredictionParams
from ml_project.models.utils.persistence_manager import PersistenceModelManager
logger = logging.getLogger()


class PredictionProcess:
    def __init__(self, prediction_config_dir: str):
        self.PredictionSchema = class_schema(PredictionParams)()

        with open(prediction_config_dir, 'r') as f:
            self.params: PredictionParams = self.PredictionSchema.load(yaml.safe_load(f))

        path_to_ml_project = os.path.dirname(__file__) + '/../'
        self.model = PersistenceModelManager.deserialize_model_from_file(path_to_ml_project +
                                                                         self.params.model_file)

    def start(self, data):
        self.predictions = self.model.predict(data)
        return self.predictions

    def health_checker(self):
        return True

    # ToDo: isolate save logic in PersistanceDataManager class in persistance_manager.py module
    def save(self):
        pd.DataFrame(data=self.predictions).to_csv(self.params.output_predictions_file)


if __name__ == '__main__':
    PredictionSchema = class_schema(PredictionParams)
    logger.info('Start prediction process')

    prediction_config = '../confs/prediction_confs/pred_conf_1.yaml'
    with open(prediction_config, 'r') as f:
        schema = PredictionSchema()
        params: PredictionParams = schema.load(yaml.safe_load(f))

    input_features_file = params.input_data_file
    with open(input_features_file, 'r') as f:
        input_features = pd.read_csv(f)

    prediction_process: PredictionProcess = PredictionProcess(prediction_config)
    prediction_process.start(input_features)
    prediction_process.save()

    logger.info('End prediction process')
