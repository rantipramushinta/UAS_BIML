import requests

url = 'http://localhost:5000/House_Price'
r = requests.post(url,json={'Area(in sq. ft)', 'Price(in Rs.)'})

print(r.json())
