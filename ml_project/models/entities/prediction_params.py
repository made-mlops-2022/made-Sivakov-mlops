from dataclasses import dataclass
from ml_project.models.utils.implemented_models import ImplementedModels


@dataclass()
class PredictionParams:
    input_data_file: str
    model_file: str
    model_type: ImplementedModels
    output_predictions_file: str
