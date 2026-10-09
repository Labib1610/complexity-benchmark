def solve():
    n = int(input())
    d = list(map(int, input().split()))
    
    total_sum = sum(d)
    if total_sum % 2 != 0:
        print("NO")
        return
    
    target_sum = total_sum // 2
    
    def find_subset(arr, target):
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in arr:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        if not dp[target]:
            return None
        
        subset = []
        i = target
        for num in reversed(arr):
            if i >= num and dp[i - num]:
                subset.append(arr.index(num) + 1)
                i -= num
        
        return subset
    
    subset1 = find_subset(d, target_sum)
    
    if subset1 is None:
        print("NO")
        return
    
    print("YES")
    print(*subset1)

solve()