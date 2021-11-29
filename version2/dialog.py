from luis import getIntent
import requests
import constants

def getResponse(query, step):
    response=''
    intent, entity = getIntent(query)
    
    if intent == 'HOLA':
        response='Hola'
        step=0
    elif intent == 'ADIOS':
        response='Adios'
        step=0
    elif intent == 'TIEMPO' and entity == None:
        response='Vamos a ver qué tiempo hace... Dime el código postal de la localidad que quieres consultar (Ej. 10002)'
        step=1
    elif intent == 'TIEMPO' and entity != None:
        r=requests.get('https://api.openweathermap.org/data/2.5/weather?zip='+entity+',es&appid='+constants.OPENWEATHER_TOKEN)
        if r.status_code==200:
            temp = r.json()['main']['temp']
            response='La temperatura es de '+str(round(temp-273.5,1))+' grados Celsius'
            step=0
        else:
            response='El código postal introducido es erróneo. Vuelva a intentarlo.'
    elif step!=0 and intent=='ZIPCODE':
        r=requests.get('https://api.openweathermap.org/data/2.5/weather?zip='+entity+',es&appid='+constants.OPENWEATHER_TOKEN)
        if r.status_code==200:
            temp = r.json()['main']['temp']
            response='La temperatura es de '+str(round(temp-273.5,1))+' grados Celsius'
            step=0
        else:
            response='El código postal introducido es erróneo. Vuelva a intentarlo.'
    else:
        response='Lo siento, no puedo ayudarte con eso en este momento.'

    return response, step