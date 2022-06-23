from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers="localhost:9092")
producer.send('sample', b'Hello, World')
producer.flush()

