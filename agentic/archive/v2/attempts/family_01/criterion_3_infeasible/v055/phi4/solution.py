import sys

def find_minimal_mutual_triplet():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    
    # Create adjacency list
    adj_list = {i: set() for i in range(1, n + 1)}
    for u, v in edges:
        adj_list[u].add(v)
        adj_list[v].add(u)

    # Try all combinations of a, b, c
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if b not in adj_list[a]:
                continue
            for c in range(b + 1, n + 1):
                if c in adj_list[a] and c in adj_list[b]:
                    print(a, b, c)
                    return

find_minimal_mutual_triplet()