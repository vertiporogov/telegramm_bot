from datetime import datetime
import requests
import json

import os

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
def main():
    while True:
        currency = input('Введите название валюты (USD или EUR)')
        if currency not in ('USD', 'EUR'):
            print('Некорректный ввод')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now()

        print(f'Курс {currency} к рублю: {rate}')
        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)

        choice = input('Выберите действие (1 - продолжить, 2 - выйти) ')
        if choice == '1':
            continue
        elif choice == '2':
            break
        else:
            print('Неверный ввод')
            # continue

def get_currency_rate(base: str) -> float:
    '''Получает курс от API и возвращает его в виде float'''
    url = "https://api.apilayer.com/exchangerates_data/latest"

    response = requests.get(url, headers={'apikey': API_KEY}, params={'base': base})
    print(response.json())

def save_to_json(date):
    pass

if __name__ == '__main__':
    get_currency_rate('USD')
    # main()