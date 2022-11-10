import logging
from sklearn.metrics import f1_score, accuracy_score
import pandas as pd
logger = logging.getLogger()


def evaluate(y_pred: pd.DataFrame, y_true: pd.DataFrame):
    logger.info('Start eval process')
    y_true = y_true.drop(columns=['Unnamed: 0'])
    y_pred = y_pred.drop(columns=['Unnamed: 0'])
    f1 = f1_score(y_true=y_true, y_pred=y_pred)
    accuracy = accuracy_score(y_true=y_true, y_pred=y_pred)
    logger.info(f'accuracy_score: {accuracy}, f1_score: {f1}')
    logger.info('End of eval process')


# class EvaluationProcess:
#     def __init__(self):
#         pass
#
#     def start(self):
#         pass
#
#     def save(self):
#         pass
#
#
# if __name__ == '__main__':
#     pass