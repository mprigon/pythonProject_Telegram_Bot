TOKEN = "5729482068:AAFnE0NgA0ng1rsNUnNrwlZGqNXXpVi3BW4"


# возможных валют больше, но неудобно писать название в двух словах,
# взяты наиболее известные
keys = {
    "биткойн": "BTC",
    "лира": "TRY",
    "юань": "CNY",
    "евро": "EUR",
    "рубль": "RUB",
    "доллар": "USD",
    "шекель": "ILS"
}

# параметры для API бесплатного accout mprigon@yandex.ru на https://api.apilayer.com
payload = {}
headers = {
  "apikey": "6EH8XOkX5tYj7Fy6klsYzC65IAaEeNme"
}

# перечень ошибок, о которых сообщает в ответе apilayer.com
# https://apilayer.com/marketplace/exchangerates_data-api?e=Sign+In&l=Success#errors
key_api_errors = {
    "400": "400 - Bad Request. The request was unacceptable, often due to missing a required parameter.",
    "401": "401 - Unauthorized. No valid API key provided.",
    "404": "404 - Not Found. The requested resource doesn't exist.",
    "429": "429 - Too many requests. API request limit exceeded. See section Rate Limiting for more info.",
    "5XX": "5XX - We have failed to process your request. (You can contact us anytime)"
}
