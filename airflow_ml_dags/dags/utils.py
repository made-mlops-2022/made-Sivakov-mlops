from datetime import timedelta

airflow_ml_dags_path = "/Users/kr.sivakov/Documents/MADE/ml_ops/hw1/airflow_ml_dags"


default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}