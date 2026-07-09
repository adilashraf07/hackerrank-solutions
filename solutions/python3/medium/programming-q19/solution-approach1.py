# ──────────────────────────────────────────────────
# Problem     TeamRoomOfPlayers
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 11:00 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input().strip()

chairs = 0
available = 0

for ch in s:
    if ch == 'C' or ch == 'U':
        if available > 0:
            available -= 1
        else:
            chairs += 1
    elif ch == 'R' or ch == 'L':
        available += 1

print(chairs)
