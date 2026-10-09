import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    flagged = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    total_energy = 0
    
    def dfs(u, parent):
        nonlocal total_energy
        count = 1 if u in flagged else 0
        for v, w in adj[u]:
            if v == parent:
                continue
            child_count = dfs(v, u)
            if child_count > 0 and child_count < t:
                total_energy += w
            count += child_count
        return count
    
    # Start from any flagged node
    start = next(iter(flagged))
    dfs(start, -1)
    
    print(total_energy)

if __name__ == "__main__":
    solve()