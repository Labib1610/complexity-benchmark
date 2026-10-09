from itertools import combinations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    relays = []
    index = 2
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        relays.append((a, b, c))
        index += 3
    
    target_sum = (1 << k) - 1  # 2^k - 1
    
    # Try all combinations of k relays
    for combo in combinations(range(t), k):
        sum1 = sum2 = sum3 = 0
        selected_relays = []
        for i in combo:
            a, b, c = relays[i]
            sum1 += 1 << (a - 1)  # 2^(a-1)
            sum2 += 1 << (b - 1)  # 2^(b-1)
            sum3 += 1 << (c - 1)  # 2^(c-1)
            selected_relays.append((a, b, c))
        
        if sum1 == target_sum and sum2 == target_sum and sum3 == target_sum:
            print("YES")
            for relay in selected_relays:
                print(relay[0], relay[1], relay[2])
            return
    
    print("NO")

solve()