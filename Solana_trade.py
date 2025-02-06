from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.system_program import transfer, TransferParams
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
SOLANA_PRIVATE_KEY = os.getenv("SOLANA_PRIVATE_KEY")

# Solana setup
solana_client = Client("https://api.mainnet-beta.solana.com")
wallet = Keypair.from_seed(bytes.fromhex(SOLANA_PRIVATE_KEY))

# Execute a trade
def execute_trade(amount=0.1, recipient="YourWalletAddressHere"):
    txn = Transaction().add(
        transfer(TransferParams(
            from_pubkey=wallet.public_key,
            to_pubkey=recipient,
            lamports=int(amount * 1e9)
        ))
    )
    txn_signature = solana_client.send_transaction(txn, wallet)
    return txn_signature