import requests

url = 'http://localhost:5000/House_Price'
r = requests.post(url,json={'Area(in sq. ft):2, 'Price(in Rs.)':9})

print(r.json())
