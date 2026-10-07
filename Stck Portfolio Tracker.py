"""
Task: Stock Portfolio Tracker
Key concepts: dictionary, input/output, basic arithmetic, file handling
"""

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}


def build_portfolio():
    portfolio = {}

    print("Enter stock name and quantity (type 'done' to finish).")
    print(f"Available stocks: {', '.join(stock_prices.keys())}\n")

    while True:
        stock = input("Stock name: ").strip().upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not found in price list. Try again.\n")
            continue

        try:
            quantity = int(input(f"Quantity of {stock}: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print()

    return portfolio


def calculate_total(portfolio):
    total = 0
    breakdown = []

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total += value
        breakdown.append((stock, quantity, price, value))

    return breakdown, total


def display_summary(breakdown, total):
    print("\n--- Portfolio Summary ---")
    print(f"{'Stock':<8}{'Qty':<6}{'Price':<8}{'Value'}")
    for stock, quantity, price, value in breakdown:
        print(f"{stock:<8}{quantity:<6}{price:<8}{value}")
    print(f"\nTotal Investment Value: {total}")


def save_to_file(breakdown, total, filename="portfolio.txt"):
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Value\n")
        for stock, quantity, price, value in breakdown:
            file.write(f"{stock},{quantity},{price},{value}\n")
        file.write(f"\nTotal Investment Value: {total}\n")

    print(f"Saved to: {filename}")


if __name__ == "__main__":
    portfolio = build_portfolio()

    if not portfolio:
        print("No stocks entered.")
    else:
        breakdown, total = calculate_total(portfolio)
        display_summary(breakdown, total)

        save = input("\nSave results to file? (y/n): ").strip().lower()
        if save == "y":
            save_to_file(breakdown, total)