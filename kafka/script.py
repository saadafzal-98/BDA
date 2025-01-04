import csv
from kafka import KafkaProducer
import json

# Kafka configuration
KAFKA_TOPIC = "users"
KAFKA_SERVER = "localhost:9092"  # Inside the container network

# File location
CSV_FILE_PATH = r"D:\BDA_PROJECT\kafka\dataset\users.csv"

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize as JSON
)

def send_data_to_kafka():
    try:
        # Open the CSV file
        with open(CSV_FILE_PATH, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Send each row as a JSON message to Kafka
            for row in reader:
                producer.send(KAFKA_TOPIC, value=row)
                print(f"Sent: {row}")

        print(f"All data from {CSV_FILE_PATH} sent to Kafka topic {KAFKA_TOPIC} successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        producer.close()

if __name__ == "__main__":
    send_data_to_kafka()
