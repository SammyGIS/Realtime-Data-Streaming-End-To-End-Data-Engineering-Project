""""
Learning Data Streaming with Spark Worker and Master
Owner: Ajeyomi Adedoyin Samuel
Date: January 6th 2024
"""


import logging
from datetime import datetime

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import cluster
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json ,col

def create_keyspace(session):
    # create keysapce here


def create_table(session, **kwargs):
    # crate table here

def insert_table(session, **kwargs):
    # insertion here

def create_spark_connection():
    # creating spark conection
    try:
        s_conn = SparkSession.builder \
        .appName('SparkDataStreaming') \
        .config('spark.jars.packages',"con.datastax \
                .spark:spark-cassandara-connector_2.13:3.41",
                "org.apache.spark:spark-sql-kafka-0-10_2.13:3.4.1")\
        .config('spark.cassandara.connection.host','localhost')\
        .getOrCreate()

    except Exception as e:
        logging.error("Couldnt create the spark session due to exception {e}")

def create_cassandra_connection():
    # creating cassandra connnection


if __name == '__main__':
