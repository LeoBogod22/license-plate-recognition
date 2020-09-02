import requests
import base64
import json

# Sample image file is available at http://plates.openalpr.com/ea7the.jpg
IMAGE_PATH = 'at.jpg'
SECRET_KEY = 'sk_ed3d203bf4c9a7c2910ec0c0'

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v3/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data = img_base64)



try:
     print({

     'PLate': r.json()['results'][0]['plate'],
     'Brand': r.json()['results'][0]['vehicle']['make_model'][0]['name'],
     'Color': r.json()['results'][0]['vehicle']['year'][0]['name'],
     'Color': r.json()['results'][0]['vehicle']['year'][0]['name'],
     })

except:

     print("ldld")
