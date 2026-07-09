# ──────────────────────────────────────────────────
# Problem     ScalarProduct Level-1
# Difficulty  Easy
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 12:36 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
v1 = list(map(int, input().split()))
v2 = list(map(int, input().split()))

v1.sort()
v2.sort(reverse=True)

result = 0
for i in range(n):
    result += v1[i] * v2[i]
    
print(result)
