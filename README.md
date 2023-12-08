What are we doing?
Take some posts from reddit, in this case, the top posts of the r/science page and then using Airflow to deposit it as a csv file into an s3 bucket. We use Python for our main web scrapper code contained as a function inside reddit_etl.py.
Then, we write code(reddit_dag.py) to create a DAG in airflow that will execute the task of depositing the csv file into the bucket. This project was done in the PyCharm IDE. AWS t3 medium instance was used to host airflow server.
