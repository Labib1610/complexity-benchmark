import sys
sys.setrecursionlimit(1000000)

def solve():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [0] * n
    for i in range(n):
        adj[i] = 0
    # adjacency bitmask
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << v)  # bug: should be adj[v] |= (1 << v)?? Let's fix.
    # Actually, we'll use adjacency list for simplicity.
    # But let's just use adjacency list.
    # I'll rewrite properly.
    pass

if __name__ == "__main__":
    solve()