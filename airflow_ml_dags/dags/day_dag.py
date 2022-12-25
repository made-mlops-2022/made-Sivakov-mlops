import os

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount
from utils import airflow_ml_dags_path as base_path
from utils import default_args

with DAG(
        "day_dag",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:
    predict = DockerOperator(
        image="airflow-predict",
            command="--input-data-dir /data/splitted/val/{{ ds }} --output-dir /prediction/{{ ds }} --input-model-dir /models/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=base_path+"/data/",
                      target="/data",
                      type='bind'),
                Mount(source=base_path+"/prediction/",
                      target="/prediction",
                      type='bind'),
                Mount(source=base_path+"/models/",
                      target="/models",
                      type='bind')
                ]
    )

    predict