import os
import pandas as pd
from sklearn.model_selection import train_test_split
import click


@click.command("predict")
@click.option("--input-dir")
@click.option("--output-train-dir")
@click.option("--output-val-dir")
def split(input_dir: str, output_train_dir, output_val_dir):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))

    X_train, X_val, y_train, y_val = train_test_split(data.drop(columns=["target"]),
                                                      data["target"], test_size=0.3, random_state=42)

    os.makedirs(output_train_dir, exist_ok=True)
    os.makedirs(output_val_dir, exist_ok=True)

    train_df = pd.concat([X_train, pd.DataFrame(data=y_train)], axis="columns")
    train_df.to_csv(os.path.join(output_train_dir, "train_data.csv"))

    val_df = pd.concat([X_val, pd.DataFrame(data=y_val)], axis="columns")
    val_df.to_csv(os.path.join(output_train_dir, "val_data.csv"))


if __name__ == '__main__':
    split()
