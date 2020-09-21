from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator

def print_detectaFalla():
   raise Exception('¡Fallo proceso!')
  
dag = DAG('notificacionAirflow', description='Notificacion Error DAG',
    schedule_interval='* * * * *',
    start_date=datetime(2020, 3, 16),
    catchup=False,)
operator = PythonOperator(task_id='task_id', 
    python_callable=print_detectaFalla,
    email_on_failure=True, 
    email="yuleisy.zamoraserrano@externos-cl.cencosud.com",
    dag=dag)
#email_operator = EmailOperator(
 #   task_id='send_email',
  #  to="yuleisy.zamoraserrano@externos-cl.cencosud.com",
   # subject="Test Email Please Ignore",
   # html_content=None,
   #∫ dag=dag)
operator 
# > 
#email_operator