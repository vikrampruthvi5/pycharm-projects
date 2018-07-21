
import requests as req

class weather_report:

    def __init__(self, city):
        api_key = 'd5a7d29cb2272cf98d615b0f020a89ea'
        city = 'city'
        code = 'IN'
        url = 'http://api.openweathermap.org/data/2.5/forecast?q='+city+'&APPID='+api_key
        # Information retrieval
        #json_data =  req.get(url).json()
        json_data = {'id': 1269843, 'name': 'Hyderabad', 'coord': {'lat': 17.3616, 'lon': 78.4747}, 'country': 'IN', 'population': 3597816}
        print(json_data['city'])

