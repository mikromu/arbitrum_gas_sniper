import requests, time

def gas_sniper():
    print("Arbitrum gas sniper: catches insane gas bids (front-runners / liquidations)")
    while True:
        r = requests.get("https://arbiscan.io/api?module=stats&action=txlist&sort=desc")
        for tx in r.json()["result"][:15]:
            gas_price = int(tx["gasPrice"]) / 1e9
            if gas_price > 5:  # >5 gwei = something cooking
                value = int(tx["value"]) / 1e18
                print(f"GAS SPIKE {gas_price:.2f} gwei!\n"
                      f"Hash: {tx['hash']}\n"
                      f"Value: {value:.6f} ETH\n"
                      f"From: {tx['from'][:10]}...\n"
                      f"https://arbiscan.io/tx/{tx['hash']}\n"
                      f"→ Probably MEV / liquidation\n"
                      f"{'='*60}")
        time.sleep(2.8)

if __name__ == "__main__":
    gas_sniper()
