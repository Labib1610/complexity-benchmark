import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Find lexicographically smallest triangle
    # For each vertex v (ascending), for each pair of neighbors a < b (both > v),
    # check if a-b edge exists
    for v in range(1, n + 1):
        neighbors_gt = sorted(x for x in adj[v] if x > v)
        found = False
        for i in range(len(neighbors_gt)):
            a = neighbors_gt[i]
            for j in range(i + 1, len(neighbors_gt)):
                b = neighbors_gt[j]
                if b in adj[a]:
                    print(f"{v} {a} {b}")
                    return
    
    # Should not reach here given problem guarantees
    print("-1")

main()