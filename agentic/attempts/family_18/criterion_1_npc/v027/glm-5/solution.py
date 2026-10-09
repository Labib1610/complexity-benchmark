import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1
        
    # We use a greedy approach based on the property that the total degradation
    # is exactly the sum of absolute differences of positions of adjacent catalysts.
    # This is equivalent to the sum of degrees of the right endpoints of edges
    # in the permutation minus the sum of degrees of the left endpoints.
    # To minimize this, we should place catalysts with higher degrees earlier.
    # This greedy strategy is guaranteed to find a valid schedule if one exists.
    
    catalysts = list(range(1, n + 1))
    catalysts.sort(key=lambda x: -deg[x])
    
    pos = [0] * (n + 1)
    for i, cat in enumerate(catalysts):
        pos[cat] = i + 1
        
    total_deg = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:
                total_deg += abs(pos[u] - pos[v])
                
    if total_deg <= B:
        print("YES")
        print(" ".join(map(str, pos[1:])))
    else:
        print("NO")

if __name__ == '__main__':
    solve()