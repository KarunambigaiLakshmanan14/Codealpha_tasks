# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 350
}


print("Enter stock holdings (type 'done' to finish):")
portfolio = {}
while True:
    stock = input("Stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not in the list. Available: ", ", ".join(stock_prices.keys()))
        continue
    try:
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity


total_investment = 0
for stock, qty in portfolio.items():
    total_investment += stock_prices[stock] * qty


print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock] * qty}")
print(f"\nTotal Investment: ${total_investment}")


save = input("\nSave to file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Total\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            file.write(f"{stock},{qty},{price},{qty * price}\n")
        file.write(f"\nTotal Investment,,,{total_investment}\n")
    print(f"Saved to {filename}")
