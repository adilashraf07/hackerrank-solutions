# ──────────────────────────────────────────────────
# Problem     Chinese
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 12:59 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

day = list(map(int, input().split()))
night = list(map(int, input().split()))

x = int(input())

day.sort()
night.sort(reverse=True)

overtime = 0

for i in range(n):
    total = day[i] + night [i]
    if total > x :
        overtime += (total-x)*100
        
print(overtime)
