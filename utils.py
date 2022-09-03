import json
import requests
from config import keys, payload, headers, key_api_errors


class ConvertionException(Exception):  # класс ошибок пользователя
    pass

class APIServerException(Exception):  # класс ошибок от сервера apilayer
    pass

# класс, конвертирующий валюты
class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести валюту саму в себя {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}.')

        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={quote_ticker}&base={base_ticker}"

        r = requests.get(url, headers=headers, data=payload)

        # status_code - поле с кодом ошибки apilayer из Документации
        # key_api_errors - словарь ошибок api_layer
        status_code = str(r.status_code)

        if status_code in key_api_errors: # ищем все коды ошибок apilayer, кроме 5XX
            raise APIServerException(key_api_errors[status_code])
        elif 500 <= int(status_code) < 600: # о 5XX известен только диапазон кодов ошибок
            raise APIServerException(f'{status_code} {key_api_errors["5XX"]}')
        else:
            pass

        total_base = amount / json.loads(r.content)["rates"][quote_ticker] 
        # print(r.status_code)  # отладочная печать
        # print(r.text)  # отладочная печать

        return total_base

# пример отладочной печати запроса: доллар рубль 2
# 200 - код успешного завершения
# {
#     "success": true,
#     "timestamp": 1662155284,
#     "base": "RUB",
#     "date": "2022-09-02",
#     "rates": {
#         "USD": 0.016591
#     }
# }