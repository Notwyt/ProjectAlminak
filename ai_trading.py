import requests
import pandas as pd
import numpy as np
import ta  # Technical analysis library

# Function to fetch price data
def fetch_prices(symbol="SOLUSDT", limit=100):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1h&limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data, columns=['time', 'open', 'high', 'low', 'close', 'volume', '_', '_', '_', '_', '_', '_'])
        df['close'] = df['close'].astype(float)
        return df
    return None

# Function to calculate MACD & RSI
def analyze_trends(symbol="SOLUSDT"):
    df = fetch_prices(symbol)
    if df is not None:
        df['MACD'] = ta.trend.macd(df['close'])
        df['RSI'] = ta.momentum.RSIIndicator(df['close']).rsi()
        macd = df['MACD'].iloc[-1]
        rsi = df['RSI'].iloc[-1]
        return {"MACD": macd, "RSI": rsi}
    return None

# Check for buy/sell signals
def check_trade_signal(symbol="SOLUSDT"):
    trends = analyze_trends(symbol)
    if trends:
        macd = trends["MACD"]
        rsi = trends["RSI"]
        
        if macd > 0 and rsi < 30:
            return f"📈 Buy Signal for {symbol} (MACD: {macd}, RSI: {rsi})"
        elif macd < 0 and rsi > 70:
            return f"📉 Sell Signal for {symbol} (MACD: {macd}, RSI: {rsi})"
        else:
            return f"⚠️ No strong signal for {symbol}"
    return "Failed to fetch market data."

if __name__ == "__main__":
    print(check_trade_signal())