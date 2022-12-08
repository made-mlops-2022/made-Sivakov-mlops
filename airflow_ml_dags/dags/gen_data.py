# import os
# from datetime import timedelta
#
# from airflow import DAG
# from airflow.providers.docker.operators.docker import DockerOperator
# from airflow.utils.dates import days_ago
# from docker.types import Mount
#
# default_args = {
#     "owner": "airflow",
#     "email": ["airflow@example.com"],
#     "retries": 1,
#     "retry_delay": timedelta(minutes=5),
# }
#
# with DAG(
#         "docker_gen_data",
#         default_args=default_args,
#         schedule_interval="@daily",
#         start_date=days_ago(5),
# ) as dag:
#