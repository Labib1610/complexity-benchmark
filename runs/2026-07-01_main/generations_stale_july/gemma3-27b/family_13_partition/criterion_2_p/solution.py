def solve():
    n = int(input())
    d = list(map(int, input().split()))
    
    total_sum = sum(d)
    if total_sum % 2 != 0:
        print("NO")
        return
    
    target_sum = total_sum // 2
    
    for i in range(1 << n):
        machine1_sum = 0
        machine1_tasks = []
        
        for j in range(n):
            if (i >> j) & 1:
                machine1_sum += d[j]
                machine1_tasks.append(j + 1)
        
        if machine1_sum == target_sum:
            print("YES")
            print(*machine1_tasks)
            return
    
    print("NO")

solve()