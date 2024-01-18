""""
Kafka Data Stream uisng Kafka Producer
Owner: Ajeyomi Adedoyin Samuel
Date: January 6th 2024
"""
from datetime import datetime
from airflow import DAG 
from airflow.operators.python import PythonOperator
from kafka import KafkaProducer
import time
import json
import logging
import requests


def get_data():
    response = requests.get('https://randomuser.me/api')
    response = response.json()
    response_result = response['results'][0]
    return response_result

def format_data(raw_data):
    data = {}
    location = raw_data['location']
    data['first_name'] = raw_data['name']['first']
    data['last_name'] = raw_data['name']['last']
    data['gender'] = raw_data['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['postcpde'] = location['postcode']
    data['email'] = raw_data['email']
    data['username'] = raw_data['login']['username']
    data['dob'] = raw_data['dob']['date']
    data['registered_date'] = raw_data['registered']['date']
    data['phone'] = raw_data['phone']
    data['picture'] = raw_data['picture']['medium']
    return data

def stream_data():
    producer = KafkaProducer(bootstrap_servers = ['broker:29092'], max_block_ms=5000)
    current_time = time.time()
    while True:
        if time.time() > current_time + 60:
            break
        try:
                raw_data = get_data()
                response = format_data(raw_data)
                producer.send('user_created', json.dumps(response).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error Occured: {e}')
            continue

default_args = {
    'owner': 'samuel',
    'start_date':datetime(2024,1,6,10,00)
}

with DAG ('user-automation',
    default_args=default_args,
    schedule_interval = '@daily',
    catchup=False) as dag:

    streaming_task = PythonOperator (
        task_id = 'stream_data_from_api',
        python_callable = stream_data
    )
