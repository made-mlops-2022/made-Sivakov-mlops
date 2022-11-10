import yaml
import pandas as pd

from ml_project.models.preprocessing import DataPreprocessing
from ml_project.models.splitting import split_data
from ml_project.models.train import TrainProcess
from ml_project.models.entities.train_params import TrainParams
from ml_project.models.entities.preprocessed_data import PreprocessedData
from ml_project.models.entities.prediction_params import PredictionParams
from ml_project.models.predict import PredictionProcess
from ml_project.models.entities.preprocessed_reqs import PreprocessedReqs
from ml_project.models.evaluate import evaluate

from marshmallow_dataclass import class_schema
from ml_project.logger_conf import logger


if __name__ == '__main__':
    logger.info('Start example pipeline')

    # First we should preprocess our data
    DataPreprocessingSchema = class_schema(PreprocessedReqs)
    logger.info('Start of data preprocessing')

    preproc_conf = './ml_project/confs/preprocess_confs/preproc_example_1.yaml'
    with open(preproc_conf, 'r') as f:
        schema = DataPreprocessingSchema()
        params: PreprocessedReqs = schema.load(yaml.safe_load(f))

    source_data = pd.read_csv(params.source_data_file)
    data_process = DataPreprocessing(source_data, params.hot_encoding_columns, params.columns_to_delete)
    data_process.start()

    path_to_save_processed_data = './data/preprocessed_data/preproc_1.csv'
    data_process.save(path_to_save_processed_data)

    logger.info('End of data preprocessing')

    # Then we should split data
    path_to_train_data = './data/splitted_data/train_data/train_data_1.csv'
    path_to_eval_data_x = './data/splitted_data/eval_data/eval_data_1_x.csv'
    path_to_eval_data_y = './data/splitted_data/eval_data/eval_data_1_y.csv'
    split_data(path_to_save_processed_data, path_to_train_data, path_to_eval_data_x, path_to_eval_data_y)

    # Then train
    TrainParamsSchema = class_schema(TrainParams)
    logger.info('Start of train_data process')

    train_config_file = './ml_project/confs/models_confs/random_forest_train_params.yaml'
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

    logger.info('End of train_data process')

    # Then predict
    PredictionSchema = class_schema(PredictionParams)
    logger.info('Start prediction process')

    prediction_config = './ml_project/confs/prediction_confs/pred_conf_1.yaml'
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

    # Then eval
    eval_data_x = pd.read_csv('./data/pred_1.csv')
    eval_data_y = pd.read_csv('./data/splitted_data/eval_data/eval_data_1_y.csv')
    evaluate(y_pred=eval_data_x, y_true=eval_data_y)

    logger.info('End example pipeline')

