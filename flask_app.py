from flask import Flask
import requests
import ipaddress
import random

app = Flask(__name__)

@app.route('/ip')
def generate():
    a = str(random.randint(1, 255))
    b = str(random.randint(1, 255))
    c = str(random.randint(1, 255))
    d = str(random.randint(1, 255))
    targetIP = a + "." + b + "." + c + "." + d
    z = requests.get("https://ip-api.com/json/{targetIP}")
    if z.status_code == 200:
        j = z.json()
        string = j.get('query'), j.get('country'), j.get('regionName'), j.get('city'), j.get('lat'), j.get('lon')
        string = str(string)
        return string
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
