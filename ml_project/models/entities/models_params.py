from dataclasses import dataclass, field


@dataclass()
class KNeighborsClassifierParams:
    n_neighbors: int = field(default=5)


@dataclass()
class RandomForestClassifierParams:
    n_estimators: int = field(default=100)
    criterion: str = field(default='gini')
    max_depth: int = field(default=None)
    min_samples_split: int = field(default=2)
    min_samples_leaf: int = field(default=1)
