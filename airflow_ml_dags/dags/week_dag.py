import os

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount
from utils import default_args
from utils import airflow_ml_dags_path as base_path


with DAG(
        "week_dag",
        default_args=default_args,
        schedule_interval="@weekly",
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

    preprocess = DockerOperator(
        image="airflow-preprocess",
        command="--input-dir /data/raw/{{ ds }} --output-dir /data/processed/{{ ds }}",
        task_id="docker-airflow-preprocess",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=base_path+"/data/",
                      target="/data",
                      type='bind')]
    )

    split = DockerOperator(
        image="airflow-split",
        command="--input-dir /data/processed/{{ ds }} --output-train-dir /data/splitted/train/{{ ds }} --output-val-dir /data/splitted/val/{{ ds }}",
        task_id="docker-airflow-split",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=base_path+"/data/",
                      target="/data",
                      type='bind')]
    )

    train = DockerOperator(
        image="airflow-train",
        command="--input-dir /data/splitted/train/{{ ds }} --output-model-dir /models/{{ ds }}",
        task_id="docker-airflow-train",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=base_path+"/data/",
                      target="/data",
                      type='bind'),
                Mount(source=base_path+"/models/",
                      target="/models",
                      type='bind'),
                ]
    )

    validate = DockerOperator(
        image="airflow-validate",
        command="--input-data-dir /data/splitted/val/{{ ds }} --input-model-dir /models/{{ ds }} --output-data-dir /validation/{{ ds }}",
        task_id="docker-airflow-validate",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=base_path+"/data/",
                      target="/data",
                      type='bind'),
                Mount(source=base_path+"/models/",
                      target="/models",
                      type='bind'),
                Mount(source=base_path+"/validation/",
                      target="/validation",
                      type='bind')
                ]
    )

    download >> preprocess >> split >> train >> validate
