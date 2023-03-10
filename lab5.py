
import requests

# api openweathermap не работает без vpn
city_name = input('Введите название города(in english): ')
responce = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+ city_name +'&appid=fae13c51f9c994c78e0ee2faf31511e8')
                 # запрашиваю(апи сайта,метод погодаж; название города; ключ)
weather_data = responce.json()
if weather_data['cod'] == 200:  # проверяю удачность запроса и при удачном исходе вывожу
    print('Погода в', city_name)
    print('Температура', int(weather_data['main']['temp']) - 273, 'градусов по Цельсию')
    print('Влажность', weather_data['main']['humidity'], '%')
    print('Давление', weather_data['main']['pressure'], 'гПа ')
else:
    print('Город не найден')

