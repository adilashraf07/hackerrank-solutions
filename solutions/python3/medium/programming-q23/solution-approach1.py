# ──────────────────────────────────────────────────
# Problem     TwoPointerTargetCheck
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 12:12 p.m.
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
