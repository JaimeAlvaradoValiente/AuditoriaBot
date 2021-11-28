import requests

def getIntent(query):
    r = requests.get('URL'+query)
    
    return r.json()['prediction']['topIntent']