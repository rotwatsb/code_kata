import sys

def solve(stocks):
    min_price = sys.maxsize
    max_profit = 0

    for x in stocks:
        min_price = min(x, min_price)
        max_profit = max(max_profit, x - min_price)

    print(max_profit)
