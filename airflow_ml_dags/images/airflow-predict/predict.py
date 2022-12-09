import os
import pandas as pd
import click
import pickle

@click.command("predict")
@click.option("--input-data-dir")
@click.option("--input-model-dir")
@click.option("--output-dir")
def split(input_data_dir, input_model_dir, output_val_dir):
    data = pd.read_csv(os.path.join(input_data_dir, "val_data.csv"))

    X_test, y_test = data.drop(columns=['target']), data['target']

    os.makedirs(output_val_dir, exist_ok=True)

    with open(os.path.join(input_model_dir, "rf_model"), 'rb') as f:
        model = pickle.load(f)

    prediction = model.predict(X_test)
    prediction.to_csv(os.path.join(output_val_dir, 'pred_results.csv'), index=False)

if __name__ == '__main__':
    split()
