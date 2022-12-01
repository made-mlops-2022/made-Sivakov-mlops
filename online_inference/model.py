from ml_project.models.predict import PredictionProcess
import os


prediction_config = os.path.dirname(__file__) + '/../ml_project/confs/prediction_confs/online_pred_conf_2.yaml'
prediction_process: PredictionProcess = PredictionProcess(prediction_config)
