import json
import time
from datetime import datetime
from confluent_kafka import Producer

# Function to create a Kafka producer
def create_producer():
    return Producer({'bootstrap.servers': 'localhost:9092'})

# Delivery report callback
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

# Function to send messages to the specified topic
def send_messages(producer, topic):
    # Sending a test message
    test_message = {'message': 'Test message to check if consumer is running', 'timestamp': str(datetime.now())}
    producer.produce(topic, value=json.dumps(test_message), callback=delivery_report)
    producer.flush()  # Ensure the message is sent immediately
    print(f'Sent: {test_message}')

    # Generating live data
    for i in range(1, 11):  # Example: Sending 10 messages
        live_message = {'message': f'Live message {i}', 'timestamp': str(datetime.now())}
        producer.produce(topic, value=json.dumps(live_message), callback=delivery_report)
        print(f'Sent: {live_message}')
        time.sleep(1)  # Wait for 1 second before sending the next message

# Main function
if __name__ == "__main__":
    topic = 'test-topic'  # The topic to send messages to
    producer = create_producer()  # Create a Kafka producer
    send_messages(producer, topic)  # Send messages
