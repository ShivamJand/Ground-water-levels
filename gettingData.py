#import panda
import json

with open('F:\Projects\SmartCity Project\data.json') as data_file:
    data = json.load(data_file)

'''
print(data['LatLng'][10]['lat_lon'])

for i in range(0,len(data['LatLng'])):
    print(data['LatLng'][i]['lat_lon'])
    print(data['LatLng'][i]['value'])
'''

for i in range(0,len(data['LatLng'])):
    if data['LatLng'][i]['value'] < 20: #return_in_getpoints_functionRED
        return getpoints(red)           #needs to be defined
    else return getpoints(blue)         #needs to be defined
