# dags/news_dag.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2023, 1, 1),
    'catchup': False
}

with DAG(
    'news_pipeline',
    schedule_interval='0 10 * * *',  # 10h sáng mỗi ngày
    default_args=default_args,
    description='Pipeline crawl tin tức AI',
    tags=['vnexpress', 'news'],
) as dag:

    run_script = BashOperator(
        task_id='run_pipeline',
        bash_command='python /app/save_to_postgres.py'
    )
