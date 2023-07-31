import json
import os
import requests
import yfinance as yf
from bs4 import BeautifulSoup

base_url = f"https://finance.yahoo.com/quote/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
}


def get_pe_ratio(ticker):
    url = base_url + f"{ticker}?p={ticker}"
    request = requests.get(url, headers=header)
    soup = BeautifulSoup(request.content, "html.parser")
    id_text = "quote-summary"
    result = soup.find(id=id_text)
    backup = []
    for item in result.findAll("td", attrs={"class": "Ta(end) Fw(600) Lh(14px)"}):
        backup.append(item.get_text(strip=True))
    return backup[10]


def get_current_stock_price(ticker):
    url = base_url + f"{ticker}/profile?p={ticker}"
    request = requests.get(url, headers=header)
    soup = BeautifulSoup(request.content, "html.parser")
    current_price = soup.find(
        "fin-streamer", {"class": "Fw(b) Fz(36px) Mb(-4px) D(ib)"}
    ).text
    return float(current_price)


def lambda_handler(event, context):
    # TODO implement
    BOT_TOKEN = os.environ.get("TOKEN")
    BOT_CHAT_ID = os.environ.get("CHAT_ID")
    STOCK_LIST = os.environ.get("STOCK_LIST")

    stocks = STOCK_LIST.split(",")
    for each in stocks:
        try:
            value = get_pe_ratio(each)
        except:
            ticker = yf.Ticker(each)
            value = ticker.info["trailingPE"]

        if value == "N/A" or value == "∞":
            pass
        elif float(value) >= 40:
            bot_message = f"Time to sell {each}"
            send_text = (
                "https://api.telegram.org/bot"
                + BOT_TOKEN
                + "/sendMessage?chat_id="
                + BOT_CHAT_ID
                + "&parse_mode=HTML&text="
                + bot_message
            )
            response = requests.get(send_text)
            print(response)
        else:
            pass
