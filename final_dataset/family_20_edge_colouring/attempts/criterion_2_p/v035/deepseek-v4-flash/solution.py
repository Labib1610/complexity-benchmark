import sys
sys.setrecursionlimit(1 << 25)

def solve():
    import sys
    input = sys.stdin.readline
    nL, nR, m = map(int, input().split())
    edges = []
    adjL = [[] for _ in range(nL)]
    adjR = [[] for _ in range(nR)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adjL[u].append((v, i))
        adjR[v].append((u, i))
    if m == 0:
        print("YES")
        print()
        return
    # compute max degree
    degL = [len(adjL[i]) for i in range(nL)]
    degR = [len(adjR[i]) for i in range(nR)]
    k = max(max(degL) if nL else 0, max(degR) if nR else 0)
    # edge color array
    color = [0] * m

    def rec(edge_indices, k):
        # edge_indices: list of edge indices to color
        if k == 0:
            return
        if k == 1:
            for e in edge_indices:
                color[e] = 1
            return
        # split edges into two groups
        # Build adjacency for this subgraph
        # We'll use local maps for left and right vertices involved
        # But easier: we have global adjL/adjR, but we need to consider only edges in edge_indices.
        # We'll create sets of incident edges for each vertex in this subgraph.
        # Since m up to 400k, we can do O(m) per recursion level, total O(m log k)
        # We'll use dicts for left and right vertices.
        left_edges = {}
        right_edges = {}
        for e in edge_indices:
            u, v = edges[e]
            left_edges.setdefault(u, []).append(e)
            right_edges.setdefault(v, []).append(e)
        # Now assign group 0 or 1 to each edge using BFS/DFS
        group = [-1] * len(edge_indices)  # but we need mapping from edge index to group
        # We'll use a dict for edge->group
        edge_group = {}
        # We'll traverse all vertices in this subgraph
        # Use stack for iterative DFS
        visited_left = set()
        visited_right = set()
        # We'll process each component
        for u in left_edges:
            if u in visited_left:
                continue
            # start DFS
            stack = [(u, 'L', 0)]  # vertex, side, next_group
            while stack:
                node, side, g = stack.pop()
                if side == 'L':
                    if node in visited_left:
                        continue
                    visited_left.add(node)
                    # assign group to unassigned edges
                    for e in left_edges[node]:
                        if e not in edge_group:
                            edge_group[e] = g
                            # toggle g for next edge
                            g = 1 - g
                            # get neighbor
                            v = edges[e][1]
                            stack.append((v, 'R', 1 - g))  # neighbor gets opposite? Actually we need to pass the group for next vertex's edges? We'll handle toggling at each vertex.
                    # Actually the above toggling inside loop is wrong because we need to alternate per vertex, not per edge globally.
                    # Let's do properly: for each vertex, we alternate group for its incident edges.
                else:
                    if node in visited_right:
                        continue
                    visited_right.add(node)
                    for e in right_edges[node]:
                        if e not in edge_group:
                            edge_group[e] = g
                            g = 1 - g
                            u = edges[e][0]
                            stack.append((u, 'L', 1 - g))
        # But the above is messy. Let's implement a cleaner BFS/DFS.

        # We'll do:
        # For each vertex, we maintain a pointer to next group to assign.
        # We'll do a BFS over the subgraph.
        from collections import deque
        edge_group = {}
        # We'll need adjacency for this subgraph: for each vertex, list of edges.
        # We already have left_edges and right_edges.
        # We'll do BFS over vertices.
        visited = set()
        for start in list(left_edges.keys()) + list(right_edges.keys()):
            if start in visited:
                continue
            q = deque()
            q.append((start, 'L' if start in left_edges else 'R'))
            visited.add(start)
            # We'll maintain next_group per vertex? Actually we can just alternate per vertex.
            # We'll use a dict to store next group for each vertex.
            next_group = {}
            while q:
                node, side = q.popleft()
                # initialize next_group for this vertex if not present
                if node not in next_group:
                    next_group[node] = 0
                g = next_group[node]
                # get incident edges
                if side == 'L':
                    inc = left_edges[node]
                else:
                    inc = right_edges[node]
                for e in inc:
                    if e not in edge_group:
                        edge_group[e] = g
                        g = 1 - g
                        # get neighbor
                        if side == 'L':
                            nb = edges[e][1]
                            ns = 'R'
                        else:
                            nb = edges[e][0]
                            ns = 'L'
                        if nb not in visited:
                            visited.add(nb)
                            q.append((nb, ns))
                next_group[node] = g  # save for future if needed (though not needed)
        # Now split edge_indices into two lists
        group0 = []
        group1 = []
        for e in edge_indices:
            if edge_group[e] == 0:
                group0.append(e)
            else:
                group1.append(e)
        # Recursively color
        k0 = (k + 1) // 2
        k1 = k // 2
        rec(group0, k0)
        rec(group1, k1)
        # Merge: add k0 to colors of group1
        for e in group1:
            color[e] += k0

    rec(list(range(m)), k)
    # Output
    print("YES")
    print(' '.join(str(color[i]) for i in range(m)))

if __name__ == "__main__":
    solve()