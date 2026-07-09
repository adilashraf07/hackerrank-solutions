# ──────────────────────────────────────────────────
# Problem     ParenthesisMatching
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 03:56 p.m.
# Technique   stack-based-matching
# Time        O(n)
# Space       O(n)
# Trick       Use a stack to track opening braces and verify it is empty after the loop to ensure all pairs are closed.
# Hint        The for-else construct executes the else block if no break occurred.
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
