from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(
    id = 'bitcoin',
    vs_currency = 'usd',
    days = 10
)
print(bitcoin_data)

import pandas as pd

data = pd.DataFrame(bitcoin_data['prices'], columns = ['TimeStamp', 'Price'])

print(data)

data['Date'] = pd.to_datetime(data['TimeStamp'], unit = 'ms')

print(data)

candlestick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})

print(candlestick_data)

import plotly.graph_objects as go
import plotly.offline as pyo

grafico_velas_bitcoin = go.Figure(data = [go.Candlestick(
    x = candlestick_data.index,
    open = candlestick_data['Price']['first'],
    high = candlestick_data['Price']['max'],
    low = candlestick_data['Price']['min'],
    close = candlestick_data['Price']['last']
    )
])

grafico_velas_bitcoin.update_layout(xaxis_rangeslider_visible = False, xaxis_title = 'Date',
                  yaxis_title = 'Price (USD $', title = 'Bitcoin en los ultimos 30 dias')

pyo.plot(grafico_velas_bitcoin, filename = './bitcoin_candlestick_graph.html', auto_open = False)