import requests


# def valute():
#     valuter = requests.get("https://yobit.net/api/3/ticker/btc_usd")
#     response =valuter.json()
#     print(response)


def valute():
    valuter = requests.get("https://yobit.net/api/3/ticker/ltc_btc")
    valuter1 = requests.get("https://yobit.net/api/3/ticker/ltc_rur")
    response =valuter1.json()
    response1 =valuter.json()
    print(response)
    print(response1)

    
    
if __name__== "__main__":
    valute()