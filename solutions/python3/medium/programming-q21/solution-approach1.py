# ──────────────────────────────────────────────────
# Problem     AnagramCheck
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 11:50 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

s = input().strip()
t = input().strip()

if Counter(s) == Counter(t):
    print("true")
else:
    print("false")
