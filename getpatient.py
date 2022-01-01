import requests
from fhirclient import client
settings = {
    'app_id': 'my_web_app',
    #'api_base': 'http://hapi.fhir.org/baseR4'
    'api_base':  'https://r4.test.pyrohealth.net/fhir'
}
smart = client.FHIRClient(settings=settings)
#smart.ready
#smart.prepare()
#print(smart.ready)
#print(smart.authorize_url)

import fhirclient.models.patient as p
import fhirclient.models.humanname as hn
import fhirclient.models.fhirdate as fdate
import json

search = p.Patient.where(struct={'name':'Puddling'})
patients = search.perform_resources(smart.server)

for pt in patients:
    print(pt.id)

#mypatient = patients[0]

""" mypatient = p.Patient()

name = hn.HumanName()
name.given = ['Juraj']
name.family = 'Puddling'

mypatient.name = [name]
mypatient.birthDate = fdate.FHIRDate('1980-02-02')
mypatient.gender = 'male'

print(json.dumps(mypatient.as_json()))
try:
    resp = smart.server.post_json('Patient',mypatient.as_json())
    print(resp)
except requests.exceptions.HTTPError as e:
    print(e) """