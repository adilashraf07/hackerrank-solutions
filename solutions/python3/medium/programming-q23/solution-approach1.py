# ──────────────────────────────────────────────────
# Problem     TwoPointerTargetCheck
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 12:12 p.m.
# Technique   two-pointer-search
# Time        O(n)
# Space       O(1)
# Trick       Exploit the sorted property by moving pointers inward based on the sum comparison to target.
# Hint        Use the while-else construct to handle the not-found case cleanly.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
nums = list(map(int, input().split()))
target = int(input())

left = 0
right = len(nums)-1

while left < right :
    s = nums[left] + nums[right]

    if s==target:
        print("Yes")
        break 
    elif s < target:
        left+=1
    else:
        right-=1

else:
    print("No")
