from saya_bot import start_telegram_bot
from ai_trading import auto_trade
from solana_trade import execute_trade

if __name__ == "__main__":
    print("Starting Saya...")

    # Start Telegram bot
    start_telegram_bot()

    # Start AI trading
    signal = auto_trade()
    print(signal)

    # Example: Execute trade if there's a buy signal
    if "Buy Signal" in signal:
        print("Executing trade...")
        trade_result = execute_trade(amount=0.1, recipient="YourRecipientWalletAddress")
        print(f"Trade successful: {trade_result}")