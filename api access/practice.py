import requests
import _json

#r = requests.get('https://api.github.com', auth=('user', 'pass'))
#r = requests.get('https://api.github.com')
#r = requests.get('https://www.facebook.com/')
r = requests.get('https://api.data.gov.in/resource/c4edbb12-db55-4ccf-be8d-d2dcd7e5ec07?api-key=579b464db66ec23bdd00000146e9ac1958cb44685120fa63e6c5d6f0&format=json&offset=0')

print(r.status_code)  # 200
#print(r.encoding)
data = r.json()
#print(data)

for i in range(0,len(data['fields'])):
    print(data['fields'][i]['name'])
#print(data.fields["name"])
#print(data.records)
#print(r.text)  # 'application/json'


