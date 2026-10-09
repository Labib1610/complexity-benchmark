import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    triples = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triples.append((a, b, c))
    
    n = 3 * q
    adj = defaultdict(list)
    for idx, (a, b, c) in enumerate(triples):
        adj[a].append((b, c, idx))
        adj[b].append((a, c, idx))
        adj[c].append((a, b, idx))
    
    used_triple = [False] * t
    used_node = [False] * (n + 1)
    result = []
    
    # Greedy: repeatedly find a node with degree 1 or pick any available triple
    changed = True
    while changed and len(result) < q:
        changed = False
        for v in range(1, n + 1):
            if used_node[v]:
                continue
            # Find an unused triple containing v
            for b, c, idx in adj[v]:
                if used_triple[idx]:
                    continue
                if used_node[b] or used_node[c]:
                    continue
                # Use this triple
                used_triple[idx] = True
                used_node[v] = True
                used_node[b] = True
                used_node[c] = True
                result.append((v, b, c))
                changed = True
                break
            if changed:
                break
    
    if len(result) == q:
        print("YES")
        for a, b, c in result:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()