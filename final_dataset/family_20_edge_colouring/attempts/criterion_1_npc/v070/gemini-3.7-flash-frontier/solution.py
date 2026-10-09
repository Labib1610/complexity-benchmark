import sys

# Increase recursion depth for deep search trees
sys.setrecursionlimit(20000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj_v = [[] for _ in range(n + 1)]
    idx = 2
    for e in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj_v[u].append(e)
        adj_v[v].append(e)
    
    # Build edge-to-edge adjacency in the line graph
    adj_e = [[] for _ in range(m)]
    for e, (u, v) in enumerate(edges):
        neighbors = set()
        for ne in adj_v[u]:
            if ne != e:
                neighbors.add(ne)
        for ne in adj_v[v]:
            if ne != e:
                neighbors.add(ne)
        adj_e[e] = list(neighbors)

    color = [0] * m
    avail = [7] * m  # Bitmask: bit 1 (val 1), bit 2 (val 2), bit 3 (val 4)
    
    # Connected components of edges
    visited_e = [False] * m
    components = []
    for e in range(m):
        if not visited_e[e]:
            comp = []
            queue = [e]
            visited_e[e] = True
            for curr in queue:
                comp.append(curr)
                for nxt in adj_e[curr]:
                    if not visited_e[nxt]:
                        visited_e[nxt] = True
                        queue.append(nxt)
            components.append(comp)

    def bit_count(x):
        return (x & 1) + ((x >> 1) & 1) + ((x >> 2) & 1)

    for comp in components:
        # Pick a vertex with 3 edges in this component for symmetry breaking
        u, v = edges[comp[0]]
        chosen_v = u if len(adj_v[u]) == 3 else v
        e1, e2, e3 = adj_v[chosen_v]
        
        # Stack for undoing changes during backtracking
        history = []

        def assign(e, c):
            # c in {1, 2, 3}, bitmask bit is (1 << (c - 1))
            bit = 1 << (c - 1)
            color[e] = c
            changed = []
            for ne in adj_e[e]:
                if color[ne] == 0 and (avail[ne] & bit):
                    avail[ne] &= ~bit
                    changed.append(ne)
            history.append((e, bit, changed))

        def unassign():
            e, bit, changed = history.pop()
            color[e] = 0
            for ne in changed:
                avail[ne] |= bit

        # Fix colors 1, 2, 3 for the 3 edges of chosen_v
        assign(e1, 1)
        assign(e2, 2)
        assign(e3, 3)

        # Check if immediate conflict
        conflict = False
        for e in comp:
            if color[e] == 0 and avail[e] == 0:
                conflict = True
                break
        if conflict:
            print("NO")
            return

        def search():
            # Find uncolored edge with minimum available colors
            min_c = 4
            best_e = -1
            all_colored = True
            
            for e in comp:
                if color[e] == 0:
                    all_colored = False
                    cnt = bit_count(avail[e])
                    if cnt == 0:
                        return False
                    if cnt < min_c:
                        min_c = cnt
                        best_e = e
                        if cnt == 1:
                            break
            
            if all_colored:
                return True
            
            mask = avail[best_e]
            for c in (1, 2, 3):
                if mask & (1 << (c - 1)):
                    assign(best_e, c)
                    if search():
                        return True
                    unassign()
            
            return False

        if not search():
            print("NO")
            return

    print("YES")
    print(*(color[i] for i in range(m)))

if __name__ == '__main__':
    solve()