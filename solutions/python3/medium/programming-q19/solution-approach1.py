# ──────────────────────────────────────────────────
# Problem     TeamRoomOfPlayers
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 11:00 a.m.
# Technique   greedy-counter-scan
# Time        O(n)
# Space       O(1)
# Trick       Track available seats and increment required chairs only when a player arrives and no seats are currently free.
# Hint        Greedy approach handles state transitions in a single pass.
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
