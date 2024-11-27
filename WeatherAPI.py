import requests
import os
from dotenv import load_dotenv
load_dotenv()
def weather():
        
    key: str = os.getenv("key")
    city = input("City: ")

    url =  f"http://api.weatherapi.com/v1/forecast.json?key={key}&q={city}&days=1&aqi=no&alerts=no"



    response = requests.get(url)
    obj = response.json()
    return obj
def main():
    obj = weather()        
    day = obj['forecast']['forecastday'][0]['day'] 
    print(obj)
    print("Max Temp:"+str(day['maxtemp_c']),"Min Temp:"+str(day['mintemp_c']),"Avg Temp:"+str(day['avgtemp_c']),sep="\n")

main()