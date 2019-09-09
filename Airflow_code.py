#Importing required modules

import datetime as dt 
import airflow
import DAG from airflow
import BashOperator,PythonOperator from airflow.operators 
import datetime, timedelta from datetime 


#Define Deafult Arguments
default_args = {
    'owner' : 'airflow',
    'Start_Date' : airflow.utils.dates.days_ago(1),
    'depends_on_past' : True,
    'email' : [sindhoora.rayapaneni23@gmail.com],
    'email_on_failure' : False,
    'email_on_retry' : False,
    'retries' : 1
    'retry_delay ' : timedelta(minutes=5)

}

#Instantiate the DAG
dag = DAG(
    'test'
    default_args=default_args,
    description = 'A DAG to test the Data Wharehouse Project',
)

#Layout all the tasks in the workflow
task1= BashOperator(
    task_id='Countries_export',
    bash_command='python Countries_data_export.py',
    dag=dag)

task2= BashOperator(
    task_id='Verifiers_export',
    bash_command='python Verifiers_data_export.py',
    dag=dag)

task3= BashOperator(
    task_id='Sessions_export',
    bash_command='python Sessionss_data_export.py',
    dag=dag)

task4= BashOperator(
    task_id='Events_export',
    bash_command='python Events_data_export.py',
    dag=dag)

task5= BashOperator(
    task_id='Countries_load',
    bash_command='python Countries_dim_load.py',
    dag=dag)

task6= BashOperator(
    task_id='Verifiers_load',
    bash_command='python Verifiers_dim_load.py',
    dag=dag)

task7= BashOperator(
    task_id='Sessions_load',
    bash_command='python Sessions_dim_load.py',
    dag=dag)

task8= BashOperator(
    task_id='Events_load',
    bash_command='python Events_dim_load.py',
    dag=dag)

task9= BashOperator(
    task_id='Fact_load',
    bash_command='python Time_Fact_table_Data_load.py',
    dag=dag)

#Settingup the Dependency
task1>>task5
task2>>task6
task3>>task7
task4>>task8
task9<<task5<<task6<<task7<<



