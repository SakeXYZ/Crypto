from django.shortcuts import render
from django.http import JsonResponse
import requests
from crypto.models import Currency
import yaml


# Загружаем ссылки из файла YAML
def load_links_from_yaml():
    with open('crypto/link.yaml', 'r') as file:
        links = yaml.safe_load(file)
    return links


# Пример использования
links = load_links_from_yaml()

# Привязка URL к каждой криптовалюте
BinanceBTCUSDT = links['BinanceBTCUSDT']
BinanceETHUSDT = links['BinanceETHUSDT']
BinanceLTCUSDT = links['BinanceLTCUSDT']


# Функция для получения цен
def get_price(request):
    prices = {}

    # Получаем цену для BTC
    response_btc = requests.get(BinanceBTCUSDT)
    if response_btc.status_code == 200:
        data_btc = response_btc.json()
        btc_price = data_btc.get("price", "Неизвестно")
        prices['BTC'] = btc_price
        # Сохраняем в базу
        Currency.objects.create(name='BTC/USDT', price=btc_price, exchange='Binance')

    # Получаем цену для ETH
    response_eth = requests.get(BinanceETHUSDT)
    if response_eth.status_code == 200:
        data_eth = response_eth.json()
        eth_price = data_eth.get("price", "Неизвестно")
        prices['ETH'] = eth_price
        # Сохраняем в базу
        Currency.objects.create(name='ETH/USDT', price=eth_price, exchange='Binance')

    # Получаем цену для LTC
    response_ltc = requests.get(BinanceLTCUSDT)
    if response_ltc.status_code == 200:
        data_ltc = response_ltc.json()
        ltc_price = data_ltc.get("price", "Неизвестно")
        prices['LTC'] = ltc_price
        # Сохраняем в базу
        Currency.objects.create(name='LTC/USDT', price=ltc_price, exchange='Binance')

    # Возвращаем цены в формате JSON
    return JsonResponse(prices)


# Главная страница
def index(request):
    return render(request, 'index.html')
