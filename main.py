import requests
import urllib.request
from PIL import Image

response = requests.get('https://apod.nasa.gov/apod/astropix.html').text
url = 'https://apod.nasa.gov/apod/'
image = ''
i = response.find('IMG SRC=')+9
while response[i] != '"':
    image += response[i]
    i += 1   # беру ссылку на картинку из того "текста который мне вернули"

image_url = url + image
print(image_url)
urllib.request.urlretrieve(image_url, "photo.jpg")  #  скачиваю фото с сайта в свою папку


img = Image.open("photo.jpg")
img.show()    # открываю