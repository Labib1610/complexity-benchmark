import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    triples = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triples.append((a, b, c))
    
    n = 3 * q
    
    # Build adjacency: for each pair (u,v), which triples contain both
    pair_to_triples = {}
    for idx, (a, b, c) in enumerate(triples):
        pairs = [(a, b), (a, c), (b, c)]
        for u, v in pairs:
            key = (u, v)
            if key not in pair_to_triples:
                pair_to_triples[key] = []
            pair_to_triples[key].append(idx)
    
    # Build adjacency: for each triple, which triples share exactly 2 elements
    adj = [[] for _ in range(t)]
    for idx, (a, b, c) in enumerate(triples):
        pairs = [(a, b), (a, c), (b, c)]
        neighbors = set()
        for u, v in pairs:
            for other_idx in pair_to_triples.get((u, v), []):
                if other_idx != idx:
                    neighbors.add(other_idx)
        adj[idx] = list(neighbors)
    
    # Find connected components
    visited = [False] * t
    components = []
    
    for start in range(t):
        if not visited[start]:
            stack = [start]
            visited[start] = True
            comp = []
            while stack:
                node = stack.pop()
                comp.append(node)
                for nb in adj[node]:
                    if not visited[nb]:
                        visited[nb] = True
                        stack.append(nb)
            components.append(comp)
    
    # For each component, check if it's a valid cluster (exactly 3 triples covering 9 distinct elements)
    clusters = []
    for comp in components:
        elements = set()
        for idx in comp:
            elements.update(triples[idx])
        if len(comp) == 3 and len(elements) == 9:
            clusters.append(comp)
    
    # Check if we have exactly q clusters covering all elements 1 to 3q
    if len(clusters) != q:
        print("NO")
        return
    
    all_elements = set()
    for comp in clusters:
        for idx in comp:
            all_elements.update(triples[idx])
    
    if all_elements != set(range(1, n + 1)):
        print("NO")
        return
    
    # Output: pick one triple from each cluster
    print("YES")
    for comp in clusters:
        idx = comp[0]
        a, b, c = triples[idx]
        print(f"{a} {b} {c}")

if __name__ == "__main__":
    solve()