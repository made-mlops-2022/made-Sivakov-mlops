from enum import Enum
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from ml_project.models.entities.models_params import RandomForestClassifierParams, KNeighborsClassifierParams
from typing import Union

#  Union of ML models. This variable is needed to maintain uniform typing.
ImplementedModelsList = Union[RandomForestClassifier,
                              KNeighborsClassifier]

#  Union of dataclasses describing required fields for models.
ImplementedModelsParams = Union[RandomForestClassifierParams,
                                KNeighborsClassifierParams]


class ImplementedModels(Enum):
    """
    Class enum for unifying access to models
    """
    KNeighborsClassifier = KNeighborsClassifier
    RandomForestClassifier = RandomForestClassifier

    @staticmethod
    def get_all_values():
        return [var.value for var in ImplementedModels]
