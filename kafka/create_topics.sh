#!/bin/bash

# Kafka broker configuration (use 9093 for internal communication)
BROKER="kafka:9093"

# Dataset folder path inside the container (update this according to your volume mount in Docker)
DATASET_FOLDER="D:/BDA_PROJECT/kafka/dataset"  # Adjust this path according to your mounted volume

# Loop through all files in the dataset folder
for file in $(ls $DATASET_FOLDER); do
  # Only process if it's a file
  if [ -f "$DATASET_FOLDER/$file" ]; then
    # Extract the topic name (file name without extension)
    topic_name=$(basename "$file" | cut -d. -f1)

    # Create the Kafka topic
    kafka-topics.sh --create --topic "$topic_name" --bootstrap-server $BROKER --partitions 3 --replication-factor 1
    echo "Created topic: $topic_name"
  fi
done

# Verify the topics
kafka-topics.sh --list --bootstrap-server $BROKER
