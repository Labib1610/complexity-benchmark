def solve():
    n, c = map(int, input().split())
    w = list(map(int, input().split()))
    
    total_weight = sum(w)
    
    if total_weight <= c:
        print(1)
        return
    
    print((total_weight + c - 1) // c)

solve()