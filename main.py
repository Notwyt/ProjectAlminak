#1  import os
2  import requests
3  import tweepy
4  import numpy as np
5  from sklearn.linear_model import LinearRegression
6  from dotenv import load_dotenv

# Load environment variables
7  load_dotenv()
8  TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
9  TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
10 ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
11 ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
12 COINGECKO_API_URL = os.getenv("COINGECKO_API_URL")

# Set up Twitter API authentication
13 auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
14 auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
15 api = tweepy.API(auth)

# Function to fetch market data
16 def get_market_data():
17     response = requests.get(COINGECKO_API_URL + "?ids=solana,bitcoin,ethereum&vs_currencies=usd")
18     return response.json()

# Function to predict market trends
19 def predict_price_trend(prices):
20     X = np.array(range(len(prices))).reshape(-1, 1)
21     y = np.array(prices)
22     model = LinearRegression()
23     model.fit(X, y)
24     future_x = np.array([[len(prices) + 1]])
25     prediction = model.predict(future_x)
26     return prediction[0]

# Function to generate tweets
27 def generate_tweet():
28     market_data = get_market_data()
29     sol_price = market_data["solana"]["usd"]
30     btc_price = market_data["bitcoin"]["usd"]
31     eth_price = market_data["ethereum"]["usd"]
32     
33     predicted_price = predict_price_trend([sol_price - 5, sol_price - 3, sol_price])  # Sample past prices
34     tweet_text = f"🚀 Market Update 🚀\n" \
35                  f"Solana: ${sol_price} (Predicted: ${round(predicted_price, 2)})\n" \
36                  f"Bitcoin: ${btc_price}\n" \
37                  f"Ethereum: ${eth_price}\n" \
38                  f"#Crypto #Solana #Bitcoin #Ethereum"

39     return tweet_text

# Function to post on Twitter
40 def post_to_twitter():
41     tweet = generate_tweet()
42     api.update_status(tweet)
43     print("Tweet posted successfully!")

# Run every hour
44 if __name__ == "__main__":
45     while True:
46         post_to_twitter()
47         print("Waiting for next update...")
48         time.sleep(3600)  # Runs every hour (3600 seconds)