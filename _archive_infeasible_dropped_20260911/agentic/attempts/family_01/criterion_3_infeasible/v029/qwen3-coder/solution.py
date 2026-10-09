import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        edges.append((u, v))
        index += 2
    
    # Build adjacency list and set for fast lookup
    adj_list = defaultdict(set)
    adj_set = set()
    for u, v in edges:
        adj_list[u].add(v)
        adj_list[v].add(u)
        adj_set.add((min(u,v), max(u,v)))
    
    # Get all nodes and sort them for deterministic processing
    nodes = sorted(adj_list.keys())
    
    best_triad = None
    
    # For each node a, look at its neighbors b
    # For each neighbor b of a, look at the neighbors c of b
    # Check if c is also a neighbor of a => triangle formed
    for a in nodes:
        neighbors_a = sorted(list(adj_list[a]))
        for i, b in enumerate(neighbors_a):
            # Only consider b > a to avoid duplicate checks
            if b <= a:
                continue
            neighbors_b = adj_list[b]
            # Check common neighbors of a and b
            for c in neighbors_b:
                if c > b and c in adj_list[a]:
                    # Found a triangle: a-b, b-c, a-c
                    triad = (a, b, c)
                    if best_triad is None or triad < best_triad:
                        best_triad = triad
            # Early exit if we've found the lex smallest possible for this a
            if best_triad and best_triad[0] < a:
                break
        if best_triad and best_triad[0] < a:
            break
    
    print(best_triad[0], best_triad[1], best_triad[2])

if __name__ == "__main__":
    main()