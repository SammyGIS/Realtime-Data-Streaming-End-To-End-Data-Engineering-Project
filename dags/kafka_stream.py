from datetime import datetime
# from airflow import DAG 
# from airflow.operators.python import PythonOperator


def get_data():
    import json
    import requests

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

def stream_data():
    from kafka import KafkaProducer
    import time
    import json
    import requests

    response = get_data()
    response = format_data(response)
    
    producer = KafkaProducer(bootstrap_servers = ['localhost:9092'], max_block_ms=5000)

    producer.send('user_created', json.dumps(response).encode('utf-8'))

# default_args = {

#     'owner': 'airscholar',
#     'start_date':datetime(2024,1,3,10,00)
# }

# with DAG as ('user-automation',
#     default_args=default_args,
#     schedule_interval = '@daily',
#     catchup=False
#     ) as dag

#     streaming_task = PythonOperator(
#         task_id = 'stream_Data_api',
#         python_callable=
#     )

stream_data()