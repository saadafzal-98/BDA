# 🚀 Big Data Project Using Docker Containers

This project demonstrates a hands-on implementation of **Big Data technologies** like **Hadoop**, **Spark**, **Hive**, **Kafka**, and more using **Docker**. The goal is to create a distributed environment where each service runs in its **own container**, providing a scalable and flexible setup similar to a production environment.

Unlike outdated distributions like **Cloudera Quickstart**, which package multiple services with limited customization options, this project allows each service to run independently. This makes it easier to maintain, upgrade, and troubleshoot individual components.

---

## ⚙️ **System Requirements**

- **Docker** must be installed on your machine.
- Allocate at least **4 GB of RAM** to Docker for this project to run smoothly. **6 GB or more** is recommended for better performance.
- The project has been developed and tested using **Python** and **PySpark**.

---

## 🛠 **Technology Stack**

| Technology    | Version       |
|---------------|---------------|
| Hadoop        | 2.7.4         |
| Spark         | 2.4.1         |
| Kafka         | 2.12-2.2.1    |
| Hive          | 2.3.2         |
| ZooKeeper     | 3.4.10        |
| Jupyter       | Latest        |

---

## 📊 **Business Model**

This project simulates a **real-world e-commerce business process**:

1. A customer **checkout event** is simulated by publishing product order data to a **Kafka topic (`users`)**.
2. The event data from Kafka is processed using **Spark Streaming**.
3. The processed data is then **stored in Hadoop HDFS** using **Hive SQL queries** for reporting and analysis.
4. **Jupyter Notebooks** can be used for querying and displaying insights from the stored data.

---

## 🏃 **How to Run the Project**

### 1️⃣ **Start All Services**
Start all the required services (Hadoop, Kafka, Spark, Hive, etc.) using the **Docker Compose** file provided in the project directory. Run the following command in your terminal:

```bash
docker-compose up -d

This will start all the services in detached mode. It may take a few minutes for all the services to start up.

2️⃣ Run Kafka Producer (Simulate Checkout Process)
To simulate the customer checkout process and send product order data to a Kafka topic named users, run the following command:


docker exec -it kafka /opt/kafka/bin/kafka-console-producer.sh \
  --broker-list localhost:9092 --topic users

3️⃣ Deploy and Run Spark Streaming Job
Deploy the Spark Streaming Job to consume data from the Kafka topic and save it to Hadoop HDFS using Hive SQL.



The Spark job will:

✅ Read real-time data from the Kafka topic: users.
✅ Parse the incoming JSON data.
✅ Write batch data to Hadoop HDFS by executing Hive SQL queries.


📁 Directory Structure



BDA_PROJECT/
├── hadoop/
├── kafka/
├── spark/
├── hive/
├── jupyter/
├── docker-compose.yml
└── spark_kafka_hive.py


🌐 Accessing Services

Service	URL
Hadoop Namenode	http://localhost:50070
Spark Master	http://localhost:8080
Hive Metastore	thrift://localhost:9083
Jupyter Notebook	http://localhost:8888


🎯 Conclusion
This project provides a complete Big Data ecosystem running on Docker. It replicates a production-like environment, where each service can be maintained and upgraded independently. 
