import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # For each edge (u, v), find the smallest w > v such that w is adjacent to both u and v
    # We'll iterate over u from 0 to n-1, and for each u, consider all pairs of its neighbors
    # To find lexicographically smallest triangle, we can iterate over the smallest vertex a,
    # then the second smallest b, and check if there's a common neighbor c > b.
    
    for a in range(n):
        for b in adj[a]:
            if b <= a:
                continue
            # Find smallest c > b such that c in adj[a] and c in adj[b]
            # Since adj is a set, we can iterate over the smaller of the two sets
            if len(adj[a]) > len(adj[b]):
                iter_set = adj[b]
                other_set = adj[a]
            else:
                iter_set = adj[a]
                other_set = adj[b]
            for c in iter_set:
                if c > b and c in other_set:
                    print(a+1, b+1, c+1)
                    return

if __name__ == "__main__":
    solve()