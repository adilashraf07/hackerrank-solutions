# ──────────────────────────────────────────────────
# Problem     AnagramCheck
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 11:50 a.m.
# Technique   hash-map-counter
# Time        O(n)
# Space       O(k)
# Trick       Use collections.Counter to compare character frequencies in linear time, which is more idiomatic and concise than manual dictionary counting.
# Hint        Counter objects support direct equality comparison.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

s = input().strip()
t = input().strip()

if Counter(s) == Counter(t):
    print("true")
else:
    print("false")
