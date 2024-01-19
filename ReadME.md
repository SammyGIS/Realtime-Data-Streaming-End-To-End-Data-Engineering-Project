# Data Engineering Pipeline with Kafka, Spark, and Cassandra

## Overview
This project implements a data engineering pipeline to process data from the RandomUser API, utilizing Apache Kafka for streaming, Apache Spark for data processing, and Cassandra for data storage. The workflow is orchestrated by Apache Airflow, and the entire system is containerized using Docker Compose. PostgreSQL is also used as part of the pipeline.

## Architecture Diagram
![alt text](architecture.png)

## Components
- **Docker Compose:** The entire project is orchestrated and run using Docker Compose. It includes services for Apache Kafka, Apache Spark, Cassandra, PostgreSQL, Schema Registry, Control Center, and Airflow.

- **Airflow DAG (Directed Acyclic Graph):** The `user-automation` DAG in `kafka_stream.py` is responsible for triggering the data streaming process using the RandomUser API.

- **Kafka Stream (`kafka_stream.py`):** Retrieves data from the RandomUser API, formats it, and sends it to a Kafka topic named 'user_created' using the Kafka producer.

- **Spark Stream (`spark_stream.py`):** Listens to the 'user_created' Kafka topic, processes the data using Spark, and inserts it into a Cassandra database.

- **Cassandra Database:** Stores the processed user data in the 'created_users' table within the 'spark_streams' keyspace.

## Instructions

### Setup
1. Ensure Docker and Docker Compose are installed on your system.
2. Clone the repository: `git clone https://github.com/sammygis/Realtime-Data-Streaming-End-To-End-Data-Engineering-Project.git`
3. Navigate to the project directory: `cd Realtime-Data-Streaming-End-To-End-Data-Engineering-Project`

### Running the Pipeline
1. Start the services using Docker Compose: `docker-compose up -d`
2. Monitor the progress in the Airflow UI: http://localhost:8080
3. Data processing and streaming will be performed automatically based on the defined schedule in the Airflow DAG.

### Additional Notes
- Adjust configuration files and environment variables as needed.
- For detailed information on each component, refer to the source code and comments in `kafka_stream.py` and `spark_stream.py`.

## References
- Tutorial: [End-to-End Data Engineering](https://www.youtube.com/watch?v=GqAcTrqKcrY)
- Code Repository: [GitHub - e2e-data-engineering](https://github.com/airscholar/e2e-data-engineering)


