from requests import get


def get_actual_rate_usd():
    response = get(url='https://www.cbr-xml-daily.ru/daily_json.js')
    result = response.json()
    return result
