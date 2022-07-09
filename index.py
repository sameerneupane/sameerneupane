
from web3 import Web3, HTTPProvider

# Get your node JSON-RPC URL
json_rpc_url = input("Please enter your Ethereum mainnet JSON-RPC URL here")
web3 = Web3(HTTPProvider(json_rpc_url))
