import os
import pandas as pd
import click


@click.command("predict")
@click.option("--input-dir")
@click.option("--output-dir")
def preprocess(input_dir: str, output_dir):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))

    # It is very strange preprocessing but why not
    data = data.rename(columns={"sepal length (cm)": "sepal_length_cm",
                   "sepal width (cm)": "sepal_width_cm",
                   "petal length (cm)": "petal_length_cm",
                   "petal width (cm)": "petal_width_cm"})

    os.makedirs(output_dir, exist_ok=True)
    data.to_csv(os.path.join(output_dir, "data.csv"))


if __name__ == '__main__':
    preprocess()