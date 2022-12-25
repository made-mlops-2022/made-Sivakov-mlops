import os

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount
from utils import airflow_ml_dags_path as base_path
from utils import default_args


with DAG(
        "gen_data",
        default_args=default_args,
        start_date=days_ago(5),
) as dag:
    download = DockerOperator(
        image="airflow-download",
        command="/data/raw/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-download",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=base_path+"/data/",
                      target="/data",
                      type='bind')]
    )

    download