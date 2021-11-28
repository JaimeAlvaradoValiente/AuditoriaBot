import requests

def getIntent(query):
    r = requests.get('https://westus.api.cognitive.microsoft.com/luis/prediction/v3.0/apps/583e3902-0349-4a22-b605-06ee20b71ee8/slots/production/predict?verbose=true&show-all-intents=true&log=true&subscription-key=c48ceb559d4a45fc89cdb6336e5c0d3e&query='+query)
    if len(r.json()['prediction']['entities'])!=0:
        entity=r.json()['prediction']['entities']['$instance']['number'][0]['text']
    else:
        entity=None
    return r.json()['prediction']['topIntent'], entity