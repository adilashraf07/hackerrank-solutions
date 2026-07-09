# ──────────────────────────────────────────────────
# Problem     BuySellStocks
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 03:32 p.m.
# Technique   single-pass-tracking
# Time        O(n)
# Space       O(1)
# Trick       Track the minimum price seen so far and update the maximum profit by calculating the difference at each step.
# Hint        Use float('inf') for min_price to handle empty lists.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
prices = list(map(int, (input().split())))
min_price = prices[0]
max_profit = 0

for price in prices:
    if price < min_price:
        min_price = price
    else:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit 
print(max_profit)
