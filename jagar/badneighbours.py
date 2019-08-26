def maxDonations(donations):
    ans = 0
    N = len(donations)
    dp = []
    for i in range(N):
        dp.append(0)

    for i in range(N - 1):
        dp[i] = donations[i]
        if i > 0:
            dp[i] = max(dp[i], dp[i - 1])
        if i > 1:
            dp[i] = max(dp[i], dp[i - 2] + donations[i])
        ans = max(ans, dp[i])

        for i in range(N - 1):
            dp[i] = donations[i + 1]
            if i > 0:
                dp[i] = max(dp[i], dp[i - 1])
            if i > 1:
                dp[i] = max(dp[i], dp[i - 2] + donations[i + 1])
            ans = max(ans, dp[i])
    return ans


donations = [10, 3, 2, 5, 7, 8]
print(maxDonations(donations))
