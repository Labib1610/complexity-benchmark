import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = defaultdict(set)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Create a list of neighbors for each node
    neighbors = [set() for _ in range(n + 1)]
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    
    # For each edge (u,v), check for a common neighbor w
    # This forms a triangle u-v-w
    min_cell = None
    
    # Sort edges to help with finding lexicographically smallest
    # But we'll iterate through nodes in order instead
    for a in range(1, n+1):
        neigh_a = sorted(neighbors[a])
        # Check pairs among neighbors of a
        for i in range(len(neigh_a)):
            b = neigh_a[i]
            if b <= a:
                continue
            for j in range(i+1, len(neigh_a)):
                c = neigh_a[j]
                if c <= b:
                    continue
                # Check if b and c are connected
                if c in neighbors[b]:
                    current = (a, b, c)
                    if min_cell is None or current < min_cell:
                        min_cell = current
                    # Since we're going in order, first found is lex smallest
                    break
            if min_cell is not None:
                break
        if min_cell is not None:
            break
                
    print(min_cell[0], min_cell[1], min_cell[2])

if __name__ == "__main__":
    main()