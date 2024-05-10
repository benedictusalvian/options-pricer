import requests
from config import YOUR_API_KEY

def get_global_quote(symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={YOUR_API_KEY}"
    response = requests.get(url)
    ans = ""
    if response.status_code == 200:
        data = response.json()
        if 'Global Quote' not in data or '05. price' not in data['Global Quote']:
            print("The returned Get Global Quote API JSON is\n", data)
            ans = "Error! Index not found"
        price = data['Global Quote']['05. price']
        ans = round(float(price))
    else:
        print(f"Error: {response.status_code}")
        ans = "Server error!"
    
    try:
        ans = int(ans)
    except ValueError:
        print(f"Error: Unable to fetch the underlying market price of {symbol}. Please enter the price manually.")
        ans = round(float(input("Enter the underlying price: ")))

    return ans