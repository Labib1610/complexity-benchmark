import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

def solve():
    input_data = sys.stdin.read().strip().split()
    n, m, k, B = map(int, input_data[:4])
    special = list(map(int, input_data[4:4+k]))
    special_set = set(special)
    edges = []
    idx = 4 + k
    for _ in range(m):
        u, v, w = map(int, input_data[idx:idx+3])
        idx += 3
        edges.append((w, u-1, v-1))
    
    # Sort edges by cost
    edges.sort()
    
    dsu = DSU(n)
    mst_edges = []
    total_cost = 0
    
    # Build MST
    for w, u, v in edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, w))
            total_cost += w
    
    # Now we need to cut MST edges to separate special nodes
    # We'll remove the most expensive edges until all special nodes are isolated
    # Build MST adjacency
    adj = [[] for _ in range(n)]
    for u, v, w in mst_edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Find which special nodes are connected via MST
    # We'll do DFS from each special node to find connected special nodes
    visited = [False] * n
    comp_id = [-1] * n
    comps = []
    comp_special = []
    
    for i in range(n):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            comp = []
            has_special = False
            while stack:
                node = stack.pop()
                comp.append(node)
                if node in special_set:
                    has_special = True
                for nei, _ in adj[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)
            comps.append(comp)
            comp_special.append(has_special)
    
    # If any component has more than one special node, we need to cut inside it
    # We'll collect edges to cut: the most expensive edges in each such component
    cut_edges = []
    cut_cost = 0
    
    # For each component with >1 special node, we need to remove edges to separate them
    # We'll do a multiway cut on the MST: remove edges until each special is alone
    # This is done by finding the minimum spanning tree of the component and cutting
    # the most expensive edges that connect special nodes.
    
    # Simpler: For each component, we can find the minimal set of edges to remove
    # to separate all special nodes. Since it's a tree, we can do DFS and cut
    # edges that lead to subtrees containing special nodes.
    
    # We'll process each component separately
    for comp in comps:
        if not comp_special[comp[0]]:
            continue
        # Build subgraph for this component
        comp_set = set(comp)
        # Find special nodes in this component
        sp_in_comp = [x for x in comp if x in special_set]
        if len(sp_in_comp) <= 1:
            continue
        
        # We need to cut edges in this tree to separate these special nodes
        # Use DFS to find edges to cut
        # Build adjacency for this component
        comp_adj = {node: [] for node in comp}
        for u, v, w in mst_edges:
            if u in comp_set and v in comp_set:
                comp_adj[u].append((v, w))
                comp_adj[v].append((u, w))
        
        # DFS from each special node, cutting edges that lead to other special nodes
        # We'll do a greedy: sort edges in this component by weight descending,
        # and remove edges that still connect two special nodes.
        # This is essentially Kruskal's on the component but removing edges.
        
        # Collect all edges in this component
        comp_edges = []
        for u, v, w in mst_edges:
            if u in comp_set and v in comp_set:
                comp_edges.append((w, u, v))
        
        # Sort descending by weight
        comp_edges.sort(reverse=True)
        
        # DSU for this component
        dsu2 = DSU(n)
        # Initially all nodes separate
        # We'll try to add edges from cheapest to most expensive, but we want to cut
        # the most expensive ones that connect special nodes.
        # Actually, we want to keep the cheapest edges that don't connect two specials.
        
        # Better: We want to remove minimum total cost edges to separate specials.
        # This is equivalent to finding a minimum spanning forest where each special
        # is in its own tree. So we run Kruskal but skip edges that would connect
        # two special nodes already in the same tree.
        
        dsu3 = DSU(n)
        keep_edges = []
        for w, u, v in sorted(comp_edges):  # cheapest first
            ru, rv = dsu3.find(u), dsu3.find(v)
            if ru == rv:
                continue
            # Check if both components contain special nodes
            # We'll track special membership per root
            # For simplicity, we can just check if both u and v are special or
            # if their components contain specials.
            # We'll maintain a set of specials per root.
            # But easier: we can just try to add edge, then check if any component
            # has >1 special. If yes, skip.
            # We'll do a simpler approach: since it's a tree, we can just cut
            # the most expensive edges on paths between specials.
            # Let's do DFS from each special and cut the most expensive edge on
            # the path to another special.
            pass
        
        # Let's do a direct approach: For each special node, find the most expensive
        # edge on the path to another special node, and cut it.
        # We'll do BFS/DFS from each special to find paths.
        
        # Build tree adjacency with edge indices
        tree_adj = {node: [] for node in comp}
        edge_idx = {}
        for i, (u, v, w) in enumerate(mst_edges):
            if u in comp_set and v in comp_set:
                tree_adj[u].append((v, w, i))
                tree_adj[v].append((u, w, i))
                edge_idx[i] = (u, v, w)
        
        # For each pair of special nodes, find max edge on path and mark it
        to_cut = set()
        for i in range(len(sp_in_comp)):
            for j in range(i+1, len(sp_in_comp)):
                s1, s2 = sp_in_comp[i], sp_in_comp[j]
                # DFS from s1 to s2, track max edge
                stack = [(s1, -1, 0, None)]  # node, parent, max_w, max_edge_idx
                visited_local = set()
                while stack:
                    node, parent, max_w, max_edge = stack.pop()
                    if node == s2:
                        to_cut.add(max_edge)
                        break
                    if node in visited_local:
                        continue
                    visited_local.add(node)
                    for nei, w, ei in tree_adj[node]:
                        if nei == parent:
                            continue
                        if w > max_w:
                            stack.append((nei, node, w, ei))
                        else:
                            stack.append((nei, node, max_w, max_edge))
        
        # Now to_cut contains edge indices to cut
        for ei in to_cut:
            u, v, w = edge_idx[ei]
            cut_edges.append((u+1, v+1))
            cut_cost += w
    
    if cut_cost <= B:
        print("YES")
        print(len(cut_edges))
        for u, v in cut_edges:
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    solve()