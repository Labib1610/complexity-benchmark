from itertools import combinations

def solve():
    k, t = map(int, input().split())
    
    if k == 0:
        print("YES")
        return
    
    if t < k:
        print("NO")
        return
    
    relays = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        relays.append((a, b, c))
    
    # Try all combinations of k relays
    for combo in combinations(relays, k):
        s1 = set()
        s2 = set()
        s3 = set()
        
        for a, b, c in combo:
            s1.add(a)
            s2.add(b)
            s3.add(c)
        
        if len(s1) * len(s2) * len(s3) == k ** 3:
            print("YES")
            for relay in combo:
                print(relay[0], relay[1], relay[2])
            return
    
    print("NO")

solve()