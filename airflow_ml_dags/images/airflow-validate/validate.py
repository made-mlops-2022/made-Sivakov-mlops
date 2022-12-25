import os
import pandas as pd
import click
import pickle
from sklearn.metrics import f1_score


@click.command("validate")
@click.option("--input-data-dir")
@click.option("--input-model-dir")
@click.option("--output-data-dir")
def validate(input_data_dir, input_model_dir, output_data_dir):
    data = pd.read_csv(os.path.join(input_data_dir, "val_data.csv"))

    X_test, y_test = data.drop(columns=['target']), data['target']

    os.makedirs(output_data_dir, exist_ok=True)

    with open(os.path.join(input_model_dir, "rf_model"), 'rb') as f:
        model = pickle.load(f)

    prediction = f1_score(y_pred=model.predict(X_test), y_true=y_test, average='weighted')

    prediction_df = pd.DataFrame(columns=['f1_score'], data=[prediction])
    prediction_df.to_csv(os.path.join(output_data_dir, 'val_results.csv'), index=False)


if __name__ == '__main__':
    validate()
