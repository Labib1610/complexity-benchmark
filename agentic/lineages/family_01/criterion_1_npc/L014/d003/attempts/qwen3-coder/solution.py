import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(100000)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    adj = defaultdict(list)
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Convert to 0-indexed
    adj0 = defaultdict(list)
    for u in adj:
        for v in adj[u]:
            adj0[u-1].append(v-1)
    edges0 = [(u-1, v-1) for u, v in edges]
    
    # Colors: 1, 2, 3
    color = [0] * n
    
    def is_valid(u, c):
        for v in adj0[u]:
            if color[v] != 0:
                s = c + color[v]
                if s == 2 * c or s == 2 * color[v]:
                    return False
        return True
    
    # Sort vertices by degree descending
    deg = [(len(adj0[i]), i) for i in range(n)]
    deg.sort(reverse=True)
    order = [x[1] for x in deg]
    
    def solve(pos):
        if pos == n:
            return True
            
        u = order[pos]
        for c in [1, 2, 3]:
            if is_valid(u, c):
                color[u] = c
                if solve(pos + 1):
                    return True
                color[u] = 0
        return False
    
    if solve(0):
        print("YES")
        # Convert back to 1-indexed
        result = [str(color[i]) for i in range(n)]
        print(" ".join(result))
    else:
        print("NO")

if __name__ == "__main__":
    main()