from enum import Enum
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from typing import Union

ImplementedModelsList = Union[RandomForestClassifier,
                              KNeighborsClassifier]


class ImplementedModels(Enum):
    KNeighborsClassifier = KNeighborsClassifier
    RandomForestClassifier = RandomForestClassifier

    @staticmethod
    def get_all_values():
        return [var.value for var in ImplementedModels]
