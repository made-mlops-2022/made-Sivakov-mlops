from dataclasses import dataclass
import pandas as pd


@dataclass()
class PreprocessedData:
    X: pd.DataFrame
    y: pd.DataFrame
