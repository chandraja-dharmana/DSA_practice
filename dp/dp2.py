# Problem 2: Climbing Stairs
# You can only climb 1 or 2 steps at a time

# https://chatgpt.com/share/6ac7096c-0ef4-83e8-b889-21f9529d039b

# n=2 1+1, 2
# n=3 1+1+1, 1+2, 2+1
# n=4 1+1+1+1, 1+2+1, 2+1+1, 1+1+2, 2+2

def climb_stairs(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2 # 1+1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

n=4
print(climb_stairs(n))

