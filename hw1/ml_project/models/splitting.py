import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(path_to_preprocessed_data: str, path_to_train_data, path_to_eval_x, path_to_eval_y):
    df = pd.read_csv(path_to_preprocessed_data)

    train_df, eval_df = train_test_split(df, test_size=0.3)
    train_df.to_csv(path_to_train_data)
    print(eval_df.columns)
    eval_df_x = eval_df.drop(columns=['condition'])
    eval_df_y = eval_df['condition']
    eval_df_x.to_csv(path_to_eval_x)
    eval_df_y.to_csv(path_to_eval_y)
