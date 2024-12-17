import json
import psycopg2
from psycopg2 import sql
from confluent_kafka import Consumer, KafkaException

# Function to create a PostgreSQL database connection and table
def create_database():
    conn = psycopg2.connect(
        dbname='mydatabase',      
        user='postgres',          
        password='khsbuPOSTGRE@1154', 
        host='localhost',        
        port='5432'               
    )
    cursor = conn.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            message TEXT NOT NULL,
            timestamp TIMESTAMP NOT NULL
        )
    ''')  # Create a table if it doesn't exist
    conn.commit()
    return conn

# Function to insert a message into the database
def insert_message(conn, message):
    cursor = conn.cursor()
    insert_query = sql.SQL(''' 
        INSERT INTO messages (message, timestamp) VALUES (%s, %s)
    ''')
    cursor.execute(insert_query, (message['message'], message['timestamp']))
    conn.commit()

# Function to create a Kafka consumer
def create_consumer():
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'my-group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe(['test-topic'])  # Subscribe to the topic
    return consumer

# Function to consume messages from the Kafka topic
def consume_messages(consumer, conn):
    try:
        print("Waiting for messages...")
        while True:
            msg = consumer.poll(1.0)  # Wait for message or timeout
            if msg is None:
                continue  # No message, continue polling
            if msg.error():
                raise KafkaException(msg.error())  # Handle errors

            # Deserialize the message value
            message_value = json.loads(msg.value().decode('utf-8'))
            print(f'Received message: {message_value}')

            # Insert the message into the database
            insert_message(conn, message_value)
    except KeyboardInterrupt:
        print("Consumer interrupted, shutting down...")
    finally:
        consumer.close()  # Close the consumer
        conn.close()  # Close the database connection

# Main function
if __name__ == "__main__":
    conn = create_database()  # Create database connection and table
    consumer = create_consumer()  # Create a Kafka consumer
    consume_messages(consumer, conn)  # Start consuming messages
