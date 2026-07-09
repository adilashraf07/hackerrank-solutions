# ──────────────────────────────────────────────────
# Problem     JackFruit Festival
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 02:39 p.m.
# Technique   greedy-sort-slice
# Time        O(N log N)
# Space       O(N)
# Trick       Sort the weights in descending order and sum the first d elements to maximize the total weight collected.
# Hint        Use list slicing weights[:d] for concise summation.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

n , d = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort(reverse=True)

print(sum(weights[:d]))
