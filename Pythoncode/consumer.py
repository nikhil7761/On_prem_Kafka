from kafka import KafkaConsumer


consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='13.234.77.234:9092',
    auto_offset_reset='earliest',
    group_id=None
)

print("Waiting for messages...")

for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
