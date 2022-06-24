from flask import request, json
import pandas as pd
app = Flask(__name__)

raw_data = pd.read_csv("patients.csv")

json_data = []

from index in range(len(raw_data)):
    json_data.append(
        {
            "Id": raw_data["Id"][index],
            "FIRST": raw_data["FIRST"][index],
            "LAST": raw_data["LAST"][index],
            "MAIDEN": raw_data["MAIDEN"][index],
            "GENDER": raw_data["GENDER"][index],
            "BIRTHDATE": raw_data["BIRTHDATE"][index],
            "DEATHDATE": raw_data["DEATHDATE"][index]
        }
    )

@app.route('/Patients', methods=['GET'])
def Patients():
    content = request.json

    response = app.response_class(
        response=json.dumps({ 
            "status": True,
            "data": json_data
        }),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=3002)
