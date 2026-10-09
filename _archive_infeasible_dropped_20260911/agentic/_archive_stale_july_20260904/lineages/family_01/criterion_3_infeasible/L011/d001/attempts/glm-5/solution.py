import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate through all combinations to find the lexicographically smallest triangle
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if b in adj[a]:
                for c in range(b + 1, n + 1):
                    if c in adj[a] and c in adj[b]:
                        print(a, b, c)
                        return

if __name__ == '__main__':
    solve()