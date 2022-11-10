from models.utils.implemented_models import ImplementedModels, ImplementedModelsList
from models.entities.train_params import TrainParams
from dataclasses import asdict
import logging
logger = logging.getLogger()


class ModelsFabric:
    """
    Single class for create models
    """
    @staticmethod
    def create_model(model_type: ImplementedModels, model_params: TrainParams.model_params) -> \
            ImplementedModelsList:

        logger.debug(f'Create {model_type.name} model with params: '
                     f'{asdict(model_params)}')

        return ImplementedModels[model_type.name].value()
