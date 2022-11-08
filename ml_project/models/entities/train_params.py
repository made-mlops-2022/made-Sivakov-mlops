from dataclasses import dataclass, field
from typing import Union
from models.entities.models_params import RandomForestClassifierParams, KNeighborsClassifierParams
from models.implemented_models import ImplementedModels, ImplementedModelsList


@dataclass()
class TrainParams:
    model_type: ImplementedModels
    train_data_file: str
    output_model_file: str
    metric_path: str
    model_params: Union[RandomForestClassifierParams,
                        KNeighborsClassifierParams] = field(default=RandomForestClassifierParams)