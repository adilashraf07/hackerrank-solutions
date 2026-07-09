# ──────────────────────────────────────────────────
# Problem     CheckDuplicates
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 11:36 a.m.
# Technique   set-length-comparison
# Time        O(n)
# Space       O(n)
# Trick       Comparing the length of a set to the original list length identifies duplicates in one line by leveraging hash-based uniqueness.
# Hint        set() constructor handles deduplication in linear time.
# ──────────────────────────────────────────────────

n = int(input())
nums = list(map(int, input().split()))

if len(set(nums)) != len(nums):
    print("true")
else:
    print("false")
