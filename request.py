import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Area(in sq. ft)':9, 'Price(in Rs.)':9})

print(r.json())
