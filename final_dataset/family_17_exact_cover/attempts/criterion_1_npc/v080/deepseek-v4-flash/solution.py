import sys
sys.setrecursionlimit(10000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    triples = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        triples.append((a, b, c))
    
    n = 3 * q
    # adjacency list: for each vertex, list of triple indices
    adj = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(triples):
        adj[a].append(idx)
        adj[b].append(idx)
        adj[c].append(idx)
    
    used = [False] * n
    chosen = []
    triple_used = [False] * t
    
    # Precompute triple masks
    triple_mask = []
    for a, b, c in triples:
        triple_mask.append((1 << a) | (1 << b) | (1 << c))
    
    # For pruning: sort triples by size of adjacency? Not needed.
    
    def backtrack():
        if len(chosen) == q:
            return True
        # find first unused vertex
        v = -1
        for i in range(n):
            if not used[i]:
                v = i
                break
        if v == -1:
            return False
        # try triples containing v
        for idx in adj[v]:
            if triple_used[idx]:
                continue
            a, b, c = triples[idx]
            if used[a] or used[b] or used[c]:
                continue
            # choose
            used[a] = used[b] = used[c] = True
            triple_used[idx] = True
            chosen.append((a+1, b+1, c+1))
            if backtrack():
                return True
            # backtrack
            chosen.pop()
            triple_used[idx] = False
            used[a] = used[b] = used[c] = False
        return False
    
    if backtrack():
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()