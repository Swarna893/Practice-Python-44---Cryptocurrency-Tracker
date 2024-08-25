# Practice-Python-44---Cryptocurrency-Tracker

import requests
import matplotlib.pyplot as plt
import datetime


def get_real_time_price(crypto_id, vs_currency='usd'):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={vs_currency}'
    response = requests.get(url)
    data = response.json()
    return data[crypto_id][vs_currency]


def get_historical_data(crypto_id, vs_currency='usd', days=30):
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=days)

    start_timestamp = int(start_date.timestamp())
    end_timestamp = int(end_date.timestamp())

    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart/range?vs_currency={vs_currency}&from={start_timestamp}&to={end_timestamp}'
    response = requests.get(url)
    data = response.json()
    prices = data['prices']

    timestamps, values = zip(*prices)
    dates = [datetime.datetime.fromtimestamp(timestamp / 1000) for timestamp in timestamps]

    return dates, values


def plot_price_trend(crypto_id, vs_currency='usd', days=30):
    dates, values = get_historical_data(crypto_id, vs_currency, days)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, label=f'{crypto_id.capitalize()} Price ({vs_currency.upper()})')
    plt.title(f'{crypto_id.capitalize()} Price Trend ({days} days)')
    plt.xlabel('Date')
    plt.ylabel(f'Price ({vs_currency.upper()})')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Replace 'bitcoin' with the cryptocurrency of your choice
    crypto_id = 'ethereum'

    # Fetch real-time price
    real_time_price = get_real_time_price(crypto_id)
    print(f'Current {crypto_id.capitalize()} Price: ${real_time_price}')

    # Fetch historical data and plot trend
    plot_price_trend(crypto_id)
