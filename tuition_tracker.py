import requests

# ASU Tuition for 2026-2027 based on official data
usd_tuition = 45774  

print("\n" + "="*40)
print("   ASU LIVE TUITION TRACKER (2026-2027)")
print("="*40)

try:
    # Anlık döviz kuru verisi çekiliyor (Free Exchange Rate API)
    print("[*] Connecting to exchange rate server...")
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=10)
    data = response.json()
    
    # Dolar/TL kurunu yakala
    try_rate = data['rates']['TRY']
    total_try = usd_tuition * try_rate

    print(f"[*] Current USD/TRY Rate: {try_rate:.2f}")
    print(f"[*] Annual ASU Tuition (USD): ${usd_tuition:,}")
    print("-" * 40)
    print(f"[*] ANNUAL ASU TUITION (TRY): {total_try:,.2f} TL")
    print("-" * 40)
    print("\n[SUCCESS] Financial data integrated via API.")

except Exception as e:
    print(f"\n[!] Error: Could not retrieve live data. Details: {e}")

# Programın hemen kapanmasını engellemek için:
print("\n" + "="*40)
input("Press Enter to close the program...")