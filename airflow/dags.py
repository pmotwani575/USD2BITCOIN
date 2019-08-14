import airflow.models as af_models
import airflow.operators as af_op
from airflow.exceptions Import AirflowSensorTimeout
import logging


default_args = {
    'owner': 'pmotwani',
    'start_date': datetime(2019, 8, 11),
    'depends_on_past': False,
    'email': 'pmotwani575@gmail.com',
    'email_on_failure': 'pmotwani575@gmail.com',
    'email_on_retry': 'pmotwani575@gmail.com',
    'retries': 3,
    'retry_delay': timedelta(minutes=10)

DAG = af_models.DAG(
    dag_id = 'my_dag',
    timeout = 60,
    start_date=datetime(2019,8,11),
    schedule_interval= '0 10 * * *')
)

datafeed = PythonOperator(
    task_id='data_feed',
    provide_context=True,
    python_callable=datascript.py,
    dag=my_dag,
)

send_email = EmailOperator(
    task_id='send_email',
    to='pmotwani575@gmail.com',
    subject='task airflow complete',
    html_content="Date: {{ ds }}",
    dag=my_dag)

)
