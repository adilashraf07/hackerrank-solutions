# ──────────────────────────────────────────────────
# Problem     CheckDuplicates
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 11:36 a.m.
# ──────────────────────────────────────────────────

n = int(input())
nums = list(map(int, input().split()))

if len(set(nums)) != len(nums):
    print("true")
else:
    print("false")
