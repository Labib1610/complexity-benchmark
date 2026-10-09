import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj_set = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_set[u].add(v)
        adj_set[v].add(u)
    
    # Independent set pruning algorithm
    nodes = list(range(n))
    
    while len(nodes) > k:
        # Heuristic: remove the node with the highest degree
        # to maximize chances of keeping potential IS candidates
        best_node = -1
        best_deg = -1
        for u in nodes:
            deg = 0
            for v in nodes:
                if v in adj_set[u]:
                    deg += 1
            if deg > best_deg:
                best_deg = deg
                best_node = u
        
        nodes.remove(best_node)
    
    # Check if remaining set is independent
    # Using adjacency set for O(1) lookups
    is_independent = True
    nodes_set = set(nodes)
    for u in nodes:
        # Check intersection of adj_set[u] and nodes_set
        if any(v in nodes_set for v in adj_set[u]):
            is_independent = False
            break
    
    if is_independent:
        sys.stdout.write("YES\n")
        res = [str(x + 1) for x in nodes]
        sys.stdout.write(" ".join(res) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()