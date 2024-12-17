# **Real-Time Data Streaming Pipeline with Kafka and ETL Processing**

---

## **Topics**

- [Project Overview](#project-overview)  
- [Components](#components)  
- [Pipeline Workflow](#pipeline-workflow)  
- [Setup and Execution](#setup-and-execution)  
- [Example Output](#example-output)  
- [Conclusion](#conclusion)  


---

## **Project Overview**

This project demonstrates how to build a **real-time data streaming pipeline** using Apache Kafka and perform ETL (Extract, Transform, Load) processes on streamed data. The pipeline integrates a Kafka producer, consumer, and PostgreSQL database to simulate real-time data ingestion, storage, and transformation workflows.

**Purpose**
- To understand and implement data streaming concepts using Kafka.
- To learn how to apply ETL transformations on real-time data.
- To integrate Kafka with a relational database (PostgreSQL) for data persistence.


---

## **Components**

### **1. Kafka Producer (`kafka_producer.py`)**  
- **Purpose**: Generates and sends messages to a Kafka topic (`test-topic`).  
- **Features**:  
   - Sends a **test message** to verify consumer readiness.  
   - Simulates **real-time data** by producing messages with timestamps.  
- **Key Functions**:  
   - `create_producer()`: Creates a Kafka producer.  
   - `send_messages()`: Produces test and live messages to the topic.  

---

### **2. Kafka Consumer (`kafka_consumer.py`)**  
- **Purpose**: Consumes messages from the Kafka topic and stores them in a PostgreSQL database.  
- **Features**:  
   - Creates a PostgreSQL table (`messages`) if it doesn't exist.  
   - Inserts each consumed message into the database.  
- **Key Functions**:  
   - `create_database()`: Establishes a database connection and creates the required table.  
   - `insert_message()`: Inserts Kafka messages into the database.  
   - `consume_messages()`: Polls messages from the Kafka topic and processes them.  

---

### **3. ETL Process (`etl_process.py`)**  
- **Purpose**: Applies ETL transformations on the stored data from PostgreSQL.  
- **Features**:  
   - Extracts data from the database into a **Pandas DataFrame**.  
   - Applies transformations like filtering by timestamp and adding derived columns.  
- **Key Functions**:  
   - `create_database_connection()`: Connects to the PostgreSQL database.  
   - `load_data_to_dataframe()`: Extracts data into a DataFrame.  
   - `perform_etl()`: Applies transformations on the extracted data.  

---

## **Pipeline Workflow**

1. **Data Production**:  
   - The Kafka Producer (`kafka_producer.py`) generates and sends messages to the Kafka topic (`test-topic`).  

2. **Data Ingestion**:  
   - The Kafka Consumer (`kafka_consumer.py`) consumes messages from the topic and inserts them into a PostgreSQL table (`messages`).  

3. **Data Transformation**:  
   - The ETL Process (`etl_process.py`) extracts data from PostgreSQL into a Pandas DataFrame.  
   - Transformation steps include filtering and adding derived columns.  

---

## **Setup and Execution**

### **Prerequisites**  
- **Python 3.x**  
- **PostgreSQL** installed and running locally.  
- **Kafka** installed and running locally.  
- Required Python libraries:  
   ```bash
   pip install pandas sqlalchemy psycopg2 confluent-kafka
   ```

---

### **Execution Steps**

#### **1. Start Kafka Services**  
- Run Zookeeper:  
   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   ```  
- Start Kafka broker:  
   ```bash
   bin/kafka-server-start.sh config/server.properties
   ```

#### **2. Run Kafka Producer**  
Generates and sends messages to the topic (`test-topic`):  
   ```bash
   python kafka_producer.py
   ```

#### **3. Run Kafka Consumer**  
Consumes messages from the topic and stores them in PostgreSQL:  
   ```bash
   python kafka_consumer.py
   ```

#### **4. Run ETL Process**  
Extracts and transforms data, displaying the transformed dataset:  
   ```bash
   python etl_process.py
   ```

---

## **Example Output**

### **Producer Output**  
```plaintext
Sent: {'message': 'Test message to check if consumer is running', 'timestamp': '2024-12-18 10:00:00'}
Sent: {'message': 'Live message 1', 'timestamp': '2024-12-18 10:00:01'}
```

### **Consumer Output**  
```plaintext
Waiting for messages...
Received message: {'message': 'Live message 1', 'timestamp': '2024-12-18 10:00:01'}
Inserted into database: (1, '2024-12-18 10:00:01', 'Live message 1')
```

### **ETL Process Output**  
```plaintext
               timestamp  id           new_column
0  2024-12-18 10:00:01   1  Transformed Data

Data Schema:
timestamp    datetime64[ns]
id                   int64
new_column         object
dtype: object
```

---

## **Conclusion**
This project demonstrates a robust **real-time data streaming pipeline** using Apache Kafka and PostgreSQL. By integrating **data production, ingestion,** and **transformation,** it showcases end-to-end data processing capabilities. The modular design allows for future enhancements, such as scaling for large datasets or adding advanced analytics. This pipeline serves as a strong foundation for real-time data engineering applications, illustrating the power of Apache Kafka, PostgreSQL, and Python.


