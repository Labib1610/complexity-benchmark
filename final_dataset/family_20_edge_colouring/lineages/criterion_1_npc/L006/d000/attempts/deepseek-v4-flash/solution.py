import sys
sys.setrecursionlimit(10000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    color = [-1] * m
    # For each vertex, track used colors
    used = [0] * n  # bitmask of used colors (1,2,4 for colors 1,2,3)
    
    # Sort edges by degree of endpoints (most constrained first)
    order = list(range(m))
    order.sort(key=lambda e: len(adj[edges[e][0]]) + len(adj[edges[e][1]]), reverse=True)
    
    def backtrack(idx):
        if idx == m:
            return True
        e = order[idx]
        u, v = edges[e]
        # Try colors 1,2,3
        for c in range(1, 4):
            bit = 1 << (c-1)
            if (used[u] & bit) == 0 and (used[v] & bit) == 0:
                color[e] = c
                used[u] |= bit
                used[v] |= bit
                if backtrack(idx + 1):
                    return True
                used[u] ^= bit
                used[v] ^= bit
                color[e] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(color[i]) for i in range(m)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()