# ──────────────────────────────────────────────────
# Problem     ParenthesisMatching
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 03:56 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input().strip()
stack = []
for ch in s :
    if ch == '{':
        stack.append(ch)
    elif ch == '}':
        if not stack:
            print("Not Matching")
            break
        stack.pop()
else:
    if not stack:
        print("Matching")
    else:
        print("Not Matching")
