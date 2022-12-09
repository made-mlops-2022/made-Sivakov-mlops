import os
import pandas as pd
import click
import pickle

from sklearn.ensemble import RandomForestClassifier


@click.command("train")
@click.option("--input-dir")
@click.option("--output-model-dir")
def train(input_dir: str, output_model_dir):
    data = pd.read_csv(os.path.join(input_dir, "train_data.csv"))

    X_train, y_train = data.drop(columns=['target']), data['target']

    os.makedirs(output_model_dir, exist_ok=True)

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    with open(os.path.join(output_model_dir, "rf_model"), 'wb') as f:
        pickle.dump(clf, f)


if __name__ == '__main__':
    train()
