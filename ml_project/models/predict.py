import logging
import yaml
import pandas as pd
from marshmallow_dataclass import class_schema
from ml_project.models.entities.prediction_params import PredictionParams
from ml_project.models.utils.persistence_manager import PersistenceModelManager
logger = logging.getLogger()


class PredictionProcess:
    def __init__(self, pred_params: PredictionParams, data):
        self.model = PersistenceModelManager.deserialize_model_from_file(pred_params.model_file)
        self.data = data

    def start(self):
        self.predictions = self.model.predict(self.data)

    # ToDo: isolate save logic in PersistanceDataManager class in persistance_manager.py module
    def save(self, output_prediction_file):
        pd.DataFrame(data=self.predictions).to_csv(output_prediction_file)


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

    prediction_process: PredictionProcess = PredictionProcess(params, input_features)
    prediction_process.start()
    prediction_process.save(params.output_predictions_file)

    logger.info('End prediction process')
