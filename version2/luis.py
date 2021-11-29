import requests
import constants

def getIntent(query):
    r = requests.get(constants.url+query)
    if len(r.json()['prediction']['entities'])!=0:
        entity=r.json()['prediction']['entities']['$instance']['number'][0]['text']
    else:
        entity=None
    return r.json()['prediction']['topIntent'], entity