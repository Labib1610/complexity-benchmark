import sys

def find_audit_committee():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    edges = []
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        edges.append((u, v))
    
    # Create adjacency list for each node
    adj_list = {i: set() for i in range(1, n + 1)}
    
    for u, v in edges:
        if u < v:
            adj_list[u].add(v)
            adj_list[v].add(u)
        else:
            adj_list[v].add(u)
            adj_list[u].add(v)
    
    # Find the smallest lexicographical triplet
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if b in adj_list[a]:
                for c in range(b + 1, n + 1):
                    if c in adj_list[a] and c in adj_list[b]:
                        print(f"{a} {b} {c}")
                        return

find_audit_committee()