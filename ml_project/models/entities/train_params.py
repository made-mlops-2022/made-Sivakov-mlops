from dataclasses import dataclass, field
from models.entities.models_params import RandomForestClassifierParams
from models.utils.implemented_models import ImplementedModels, ImplementedModelsParams


@dataclass()
class TrainParams:
    model_type: ImplementedModels
    train_data_file: str
    output_model_file: str
    model_params: ImplementedModelsParams = field(default=RandomForestClassifierParams)
