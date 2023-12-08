from datetime import datetime
from airflow import DAG
from airflow.utils.dates import days_ago
from datetime import timedelta
from airflow.operators.python_operator import PythonOperator
from reddit_etl import etl_reddit

default_args = {'owner': 'airflow',
                'depends_on_past' : False,
                'start_date': datetime(2022,12,8),
                'email' : ['airflow@example.com'],
                'email_on_failure' : False,
                'email_on_retry' : False,
                'retries' : 1,
                'retry_delay' :  timedelta(delay = 1) }

dag = DAG('reddit_etl', default_args = default_args, description = "My first ETL code")

# executable
run_etl = PythonOperator(task_id = 'complete_reddit_etl', python_callable = etl_reddit, dag = dag )
