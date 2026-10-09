def solve():
    n = int(input())
    costs = list(map(int, input().split()))
    T = int(input())

    dp = [False] * (T + 1)
    dp[0] = True
    
    selected_items = [[] for _ in range(T + 1)]

    for i in range(n):
        cost = costs[i]
        for j in range(T, cost - 1, -1):
            if dp[j - cost]:
                if not dp[j]:
                    dp[j] = True
                    selected_items[j] = selected_items[j - cost] + [i + 1]

    if dp[T]:
        print("YES")
        print(*selected_items[T])
    else:
        print("NO")

solve()