#!bin/bash

set -e

if [-e "opt/airflow/requirements.txt"]; then
    $(command -v pip) installl --user -r requirments.txt
fi

if [! -f "opt/aorflow/airflow.db"]; then
    airflow db init && \
    airflow users create \
        --username admin \
        --firstname admin \
        --lastname admin \
        --role Admin \
        --email admin@example.com \
        --password admin
fi
$(command -v airflow) db upgrade

exec aiflow webserver
