from itertools import combinations

def solve():
    q, t = map(int, input().split())
    n = 3 * q
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a, b, c))
    
    # Try all combinations of q triples
    for combo_indices in combinations(range(t), q):
        used = [False] * (n + 1)
        valid = True
        selected = []
        
        for i in combo_indices:
            a, b, c = triples[i]
            if used[a] or used[b] or used[c]:
                valid = False
                break
            used[a] = used[b] = used[c] = True
            selected.append((a, b, c))
        
        if valid and all(used[i] for i in range(1, n + 1)):
            print("YES")
            for triple in selected:
                print(*triple)
            return
    
    print("NO")

solve()