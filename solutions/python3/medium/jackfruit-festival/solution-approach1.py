# ──────────────────────────────────────────────────
# Problem     JackFruit Festival
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 02:48 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

n , d = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort(reverse=True)

print(sum(weights[:d]))
