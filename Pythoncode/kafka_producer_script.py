from kafka import KafkaProducer
import logging

logging.basicConfig(level=logging.INFO)

try:
    producer = KafkaProducer(bootstrap_servers='13.234.77.234:9092')
    producer.send('test-topic', b'This is a test message from Python!')
    producer.flush()
    logging.info("Message sent successfully")
except Exception as e:
    logging.error(f"An error occurred: {e}")
