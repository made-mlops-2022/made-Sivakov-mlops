import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(path_to_preprocessed_data: str):
    df = pd.read_csv(path_to_preprocessed_data)

    train_df, eval_df = train_test_split(df, test_size=0.3)
