import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    
    protocols = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        protocols.append((a, b, c))
    
    # Build adjacency list: for each node, list of protocol indices
    adj = [[] for _ in range(n + 1)]
    for i, (u, v, w) in enumerate(protocols):
        adj[u].append(i)
        adj[v].append(i)
        adj[w].append(i)
    
    used = [False] * (n + 1)
    result = []
    
    # Greedy approach: process nodes in order, match each unused node
    for u in range(1, n + 1):
        if used[u]:
            continue
        
        # Find a protocol containing u that can be used
        found = False
        for p_idx in adj[u]:
            a, b, c = protocols[p_idx]
            if not used[a] and not used[b] and not used[c]:
                result.append((a, b, c))
                used[a] = True
                used[b] = True
                used[c] = True
                found = True
                break
        
        if not found:
            print("NO")
            return
    
    print("YES")
    for a, b, c in result:
        print(a, b, c)

if __name__ == "__main__":
    solve()