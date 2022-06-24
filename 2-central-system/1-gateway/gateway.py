from flask import request, json
from kafka import KafkaProducer
app = Flask(__name__)

@app.route('/Patients', methods=['POST'])
def Patients():
    content = request.json

    message = json.dumps(content.entry).encode("ascii")
    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    if len(content.entry) > 5:
        producer.send('gateway-hadoop', message)
    else :
        producer.send('gateway-spark', message)
    producer.flush()

    response = app.response_class(
        response=json.dumps({ "status": True }),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=3001)
