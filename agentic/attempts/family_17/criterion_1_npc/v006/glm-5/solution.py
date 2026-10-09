import sys
input = sys.stdin.readline

def solve():
    q, t = map(int, input().split())
    n = 3 * q
    
    # Read all trios
    trios = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        trios.append((a, b, c))
    
    # Build adjacency: for each pair, which trios contain it
    pair_to_trios = {}
    for idx, (a, b, c) in enumerate(trios):
        pairs = [(a, b), (a, c), (b, c)]
        for p in pairs:
            if p not in pair_to_trios:
                pair_to_trios[p] = []
            pair_to_trios[p].append(idx)
    
    # For each element, which trios contain it
    elem_to_trios = [[] for _ in range(n + 1)]
    for idx, (a, b, c) in enumerate(trios):
        elem_to_trios[a].append(idx)
        elem_to_trios[b].append(idx)
        elem_to_trios[c].append(idx)
    
    # State: which elements are used
    used = [False] * (n + 1)
    result = []
    
    # Greedy with backtracking
    def backtrack(pos):
        if pos > n:
            return True
        
        if used[pos]:
            return backtrack(pos + 1)
        
        # Try each trio containing pos
        for idx in elem_to_trios[pos]:
            a, b, c = trios[idx]
            if not used[a] and not used[b] and not used[c]:
                used[a] = used[b] = used[c] = True
                result.append((a, b, c))
                if backtrack(pos + 1):
                    return True
                result.pop()
                used[a] = used[b] = used[c] = False
        
        return False
    
    if backtrack(1):
        print("YES")
        for trio in result:
            print(trio[0], trio[1], trio[2])
    else:
        print("NO")

solve()