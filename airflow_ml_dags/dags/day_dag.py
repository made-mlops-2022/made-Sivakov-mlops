import os
from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount

default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "day_dag",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:
    predict = DockerOperator(
        image="airflow-predict",
            command="/data/raw/{{ ds }}",
        network_mode="bridge",
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source="/Users/kr.sivakov/Documents/MADE/ml_ops/hw1/airflow_ml_dags/data/",
                      target="/data",
                      type='bind'),
                Mount(source="/Users/kr.sivakov/Documents/MADE/ml_ops/hw1/airflow_ml_dags/prediction/",
                      target="/prediction",
                      type='bind')
                ]
    )

    predict