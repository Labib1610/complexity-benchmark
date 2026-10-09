from itertools import combinations

def solve():
    q, t = map(int, input().split())
    trios = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        trios.append((a, b, c))
    
    # Try all combinations of q trios from the t available trios
    for combo in combinations(range(t), q):
        used = [False] * (3 * q + 1)
        valid = True
        selected_trios = []
        
        for i in combo:
            a, b, c = trios[i]
            if used[a] or used[b] or used[c]:
                valid = False
                break
            used[a] = used[b] = used[c] = True
            selected_trios.append((a, b, c))
        
        if valid:
            print("YES")
            for trio in selected_trios:
                print(trio[0], trio[1], trio[2])
            return
    
    print("NO")

solve()