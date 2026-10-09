import sys
from collections import defaultdict, deque

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find_parent(parent, x), find_parent(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    terminals = list(map(int, data[idx:idx+t]))
    idx += t
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # Convert to 0-indexed for terminals
    terminal_set = set(x - 1 for x in terminals)
    
    # Build graph
    graph = defaultdict(list)
    for w, u, v in edges:
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    
    # Step 1: Build Steiner tree using BFS/DFS to find pairwise distances
    # We'll use a different approach: build the MST of the complete graph on terminals
    # where edge weights are shortest path distances in the original tree
    
    # Compute all-pairs shortest paths between terminals
    # Since the graph is a tree, we can do BFS from each terminal
    
    dist = {}
    parent_in_tree = {}
    
    for start in terminal_set:
        queue = deque([(start, 0, -1)])
        dist[start] = {}
        parent_in_tree[start] = {}
        while queue:
            node, d, par = queue.popleft()
            if node in dist[start]:
                continue
            dist[start][node] = d
            parent_in_tree[start][node] = par
            for nei, w in graph[node]:
                if nei != par:
                    queue.append((nei, d + w, node))
    
    # Create complete graph on terminals
    terminal_list = list(terminal_set)
    steiner_edges = []
    
    for i in range(len(terminal_list)):
        for j in range(i+1, len(terminal_list)):
            u, v = terminal_list[i], terminal_list[j]
            distance = dist[u][v]
            steiner_edges.append((distance, u, v))
    
    # Sort edges by weight
    steiner_edges.sort()
    
    # Kruskal's algorithm to find MST of terminal graph
    parent = list(range(n))
    rank = [0] * n
    cost = 0
    edges_used = 0
    
    for w, u, v in steiner_edges:
        if find_parent(parent, u) != find_parent(parent, v):
            union(parent, rank, u, v)
            cost += w
            edges_used += 1
            if edges_used == t - 1:
                break
    
    print(cost)

if __name__ == "__main__":
    main()