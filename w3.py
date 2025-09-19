import requests

API_KEY = "c385954a443de411c213b491efdef40e"
CITY = "Mardan"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL).json()
temprature = response['main']['temp']
print(f"Currect temparature in {CITY}:{temprature}C")