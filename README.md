# myconversionproject

this project contaits 3 parts

PLEASE NOTE : Details of execution the entire project is detailed mentioned in RUNBOOK.DOC


1) AIRFLOW server components in AIRFLOW Folder  

 Container airflow docker file in docker file text file
we will deploy the airflow container and then run airflow webserver over port 8080
and run airflow scheduler

Once the airflow server is up and running fine we will push our dags.py script to create DAG and create or schedule Datascript.py command in 10 minutes

PS : Additionally we can include the CMD AIRFLOW.CFG in docker file to enable the airflow server configuration . but to keep it easy I havent use that.

##########################################


2) MYSQL server components in MYSQL Folder

Once the mysql server is deployed , we will login to mysql server by below

mysql -u root -p
enter password : password to launch the sql server

Once server is launched we will create a bitcoin.py script to make a SQL connection and insert/feed the data  via Python to our Bitcoin tables

PS : Please note we are running this script from our airflow server every 10 minutes


#############################################

3) For orchestration/monitoring tasks or alerting the tasks and creating alerts for our failed tasks we can use tools such as Amazon ECS with Fargate or EC2 or Kubernetes , or we can alleasst use Docker-compose for running two dockers together and same file is mentioned in folder but it wad not working for me

PS : I am communication both the containers via Bridge netwrorking over localhost  

########################################

4) Please find the plotting.py python script which will create the scattered plot and shows the Relationship between timeline and echange rate

X AXIS : TimeLine
Y AXIS : Exchange rate

We can monitor the task and predict how strong USD vs BITCOIN market is going .
