import sys
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    color = [-1] * m
    # For each vertex, track which colors are used
    used = [set() for _ in range(n)]
    
    # Order edges by degree of endpoints (most constrained first)
    order = list(range(m))
    order.sort(key=lambda e: len(adj[edges[e][0]]) + len(adj[edges[e][1]]), reverse=True)
    
    def backtrack(idx):
        if idx == m:
            return True
        e = order[idx]
        u, v = edges[e]
        # Try colors 1,2,3
        for c in range(3):
            if c not in used[u] and c not in used[v]:
                color[e] = c
                used[u].add(c)
                used[v].add(c)
                if backtrack(idx + 1):
                    return True
                used[u].remove(c)
                used[v].remove(c)
                color[e] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()