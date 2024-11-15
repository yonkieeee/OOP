from requests import get


def get_json_currency():
    req = get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json").text
    with open("currency.json", "w") as file:
        file.writelines(req)
