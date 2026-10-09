import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    index = 3
    edges = []
    adj = defaultdict(set)
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # If there are no edges, we can pick any k nodes
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, min(k+1, n+1)))))
        return
    
    # Bipartition the graph
    color = [-1] * (n + 1)
    camp1 = []
    camp2 = []
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        camp1.append(start)
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - current_color
                    if color[neighbor] == 0:
                        camp1.append(neighbor)
                    else:
                        camp2.append(neighbor)
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    # Not bipartite, but problem guarantees it is
                    pass
    
    for i in range(1, n+1):
        if color[i] == -1:
            bfs(i)
    
    # Build complement graphs for each camp
    def build_complement(camp):
        comp_adj = defaultdict(set)
        camp_set = set(camp)
        for u in camp:
            for v in camp:
                if u != v and v not in adj[u]:
                    comp_adj[u].add(v)
        return comp_adj
    
    comp_adj1 = build_complement(camp1)
    comp_adj2 = build_complement(camp2)
    
    # Find maximum independent set in complement graph using greedy approach
    def max_independent(comp_adj, camp):
        # Greedy: sort by degree ascending and pick vertices that don't conflict
        deg = {u: len(comp_adj[u]) for u in camp}
        sorted_nodes = sorted(camp, key=lambda x: deg[x])
        selected = []
        selected_set = set()
        for u in sorted_nodes:
            # Check if u conflicts with any already selected node
            conflict = False
            for v in selected:
                if v in comp_adj[u]:
                    conflict = True
                    break
            if not conflict:
                selected.append(u)
                selected_set.add(u)
        return selected
    
    ind1 = max_independent(comp_adj1, camp1)
    ind2 = max_independent(comp_adj2, camp2)
    
    # Try to find a combination that gives us exactly k nodes
    # Since we want an independent set in the original graph,
    # we can take any subset from camp1 that's independent,
    # and any subset from camp2 that's independent,
    # and their union will still be independent (no edges within camps)
    
    # So we just need |S1| + |S2| = k where S1 ⊆ ind1, S2 ⊆ ind2
    # We can take up to len(ind1) from camp1 and up to len(ind2) from camp2
    
    max_camp1 = len(ind1)
    max_camp2 = len(ind2)
    
    # Try all combinations
    found = False
    res = []
    
    # Iterate through possible sizes from camp1
    for s1_size in range(min(max_camp1, k) + 1):
        s2_size = k - s1_size
        if 0 <= s2_size <= max_camp2:
            found = True
            res = ind1[:s1_size] + ind2[:s2_size]
            break
    
    if found:
        print("YES")
        print(' '.join(map(str, res)))
    else:
        print("NO")

if __name__ == "__main__":
    main()