import os
import pandas as pd
import numpy as np
import click
from sklearn import datasets


@click.command("download")
@click.argument("output_dir")
def download(output_dir: str):
    iris = datasets.load_iris()
    iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                           columns=iris['feature_names'] + ['target'])

    os.makedirs(output_dir, exist_ok=True)
    iris_df.to_csv(os.path.join(output_dir, "data.csv"))


if __name__ == '__main__':
    download()
