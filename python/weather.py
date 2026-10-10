import requests
lat = input("Enter the Latitute: ")
long = input("Enter the Longitute: ")
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m"
resp = requests.get(url)

temp = resp.json()

curr = temp.get("current")
todaytemp = curr.get("temperature_2m")
print(todaytemp)
