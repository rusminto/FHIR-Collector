import requests
import json
import timer

while True:
    source_url = 'http://localhost:3002/Patients'
    destination_url = 'http://localhost:3001/Patients'
    raw_data = requests.get(source_url)
    raw_json_data = json.loads(raw_data.text)

    json_data = []
    for patient in raw_json_data.data:
        json_data.append(
        {
            "resourceType": "Patient",
            "id": patient["Id"],
            "text": {
                "status": "generated",
                "div": "<div></div>"
            },
            "identifier": [
                {
                "use": "usual",
                "type": {
                    "coding": [
                    {
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                        "code": "MR"
                    }
                    ]
                },
                "system": "urn:oid:1.2.36.146.595.217.0.1"
                }
            ],
            "active": true,
            "name": [
                {
                    "use": "official",
                    "given": [
                        patient["FIRST"],
                        patient["LAST"]
                    ]
                },
                {
                    "use": "maiden",
                    "given": [
                        patient["MAIDEN"]
                    ]
                }
            ],
            "telecom": [],
            "gender": "male" if patient["GENDER"] == "M" else "female",
            "birthDate": patient["BIRTHDATE"],
            "_birthDate": {
                "extension": [
                    {
                        "url": "http://hl7.org/fhir/StructureDefinition/patient-birthTime",
                        "valueDateTime": (str(patient["Id"]) + "T00:00:00-00:00")
                    }
                ]
            },
            "deceasedBoolean": True if patient["DEATHDATE"] else False,
            "address": [],
            "contact": [],
            "managingOrganization": {}
        })

    response = requests.post(destination_url, json = json_data)
    timer.sleep(5)

