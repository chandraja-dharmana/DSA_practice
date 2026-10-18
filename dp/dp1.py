#Problem 1: Fibonacci Number

#https://chatgpt.com/share/6ac705c7-afc8-83ee-8e41-5418912aa5ca

n = 6

dp = [0] * (n + 1)

dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])

