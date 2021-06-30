import requests
filepath="C:/Users/Administrator/Desktop/1.png"
files = { 'upload': open(filepath, 'rb')}

r = requests.post('http://127.0.0.1:5000', files=files)


print(11111)