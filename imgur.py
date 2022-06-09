import requests
import json
import configparser
import pyimgur

config = configparser.ConfigParser()
config.read('auth.ini')
client_id = config.get('credentials', 'client_id')
client_secret = config.get('credentials', 'client_secret')
imgur_Access_Token = 'Bearer ' + str(config.get('credentials', 'imgur_Access_Token'))
print(imgur_Access_Token)

def upload_image(path):
  image = pyimgur.Imgur(client_id)
  uploaded_image = image.upload_image(path, title="test")
  print(uploaded_image.link)
  return uploaded_image


def upload_vedio(path):
  url = "https://api.imgur.com/3/upload"
  payload = {'album': 'ALBUMID','type': 'file', 'disable_audio': '0'}
  files = [('video', open(path,'rb'))]
  headers = {'Authorization': imgur_Access_Token}
  response = requests.request("POST", url, headers=headers, data = payload, files = files)
  data = response.json()
  print(data["data"]["link"])
  return data["data"]["link"]


