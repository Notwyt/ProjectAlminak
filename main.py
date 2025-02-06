import telebot
from flask import Flask, request
import os

# Load environment variables
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your-render-url.onrender.com/' + TOKEN)
    return "Webhook set!", 200

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🔥 MiningNexus AI Trading Bot is LIVE! 🔥")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)