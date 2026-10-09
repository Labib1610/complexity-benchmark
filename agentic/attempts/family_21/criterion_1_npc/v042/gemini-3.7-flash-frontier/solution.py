import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
    
    terminals = [int(next(it)) - 1 for _ in range(k)]
    
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w, i))
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        
    if k <= 1:
        print("YES")
        print(0)
        return

    # Dinic's algorithm for min s-t cut
    def min_cut(sources, sinks):
        # Build flow network
        # Super source S = n, Super sink T = n + 1
        S = n
        T = n + 1
        num_nodes = n + 2
        
        head = [-1] * num_nodes
        to = []
        cap = []
        flow = []
        nxt = []
        
        def add_edge(u, v, c):
            to.append(v); cap.append(c); flow.append(0); nxt.append(head[u]); head[u] = len(to) - 1
            to.append(u); cap.append(0); flow.append(0); nxt.append(head[v]); head[v] = len(to) - 1

        for u, v, w, _ in edges:
            # Bidirectional capacity w
            to.append(v); cap.append(w); flow.append(0); nxt.append(head[u]); head[u] = len(to) - 1
            to.append(u); cap.append(w); flow.append(0); nxt.append(head[v]); head[v] = len(to) - 1

        INF = 10**18
        for s in sources:
            add_edge(S, s, INF)
        for t in sinks:
            add_edge(t, T, INF)
            
        level = [-1] * num_nodes
        
        def bfs():
            for i in range(num_nodes):
                level[i] = -1
            level[S] = 0
            q = deque([S])
            while q:
                u = q.popleft()
                e = head[u]
                while e != -1:
                    v = to[e]
                    if cap[e] - flow[e] > 0 and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
                    e = nxt[e]
            return level[T] >= 0

        ptr = [0] * num_nodes
        def dfs(u, pushed):
            if pushed == 0 or u == T:
                return pushed
            e = ptr[u]
            while e != -1:
                v = to[e]
                tr = cap[e] - flow[e]
                if level[u] + 1 == level[v] and tr > 0:
                    tr = min(tr, pushed)
                    push = dfs(v, tr)
                    if push > 0:
                        flow[e] += push
                        flow[e ^ 1] -= push
                        return push
                e = nxt[e]
                ptr[u] = e
            return 0

        max_flow = 0
        while bfs():
            for i in range(num_nodes):
                ptr[i] = head[i]
            while True:
                pushed = dfs(S, INF)
                if pushed == 0:
                    break
                max_flow += pushed
                
        # Find reachable from S in residual graph
        reachable = [False] * num_nodes
        reachable[S] = True
        q = deque([S])
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] - flow[e] > 0 and not reachable[v]:
                    reachable[v] = True
                    q.append(v)
                e = nxt[e]
                
        source_set = [u for u in range(n) if reachable[u]]
        return max_flow, source_set

    # Isolating cuts heuristic
    iso_sets = []
    for i in range(k):
        src = [terminals[i]]
        snk = [terminals[j] for j in range(k) if j != i]
        _, s_set = min_cut(src, snk)
        iso_sets.append(set(s_set))

    def evaluate_partition(assignment):
        # assignment is list of length n with values 0..k-1
        cut_edges = []
        cost = 0
        for u, v, w, idx in edges:
            if assignment[u] != assignment[v]:
                cost += w
                cut_edges.append((u + 1, v + 1))
        return cost, cut_edges

    best_cost = float('inf')
    best_edges = []

    # Test isolating cut partitions
    for omit in range(k):
        assignment = [-1] * n
        for i in range(k):
            if i == omit:
                continue
            for u in iso_sets[i]:
                if assignment[u] == -1:
                    assignment[u] = i
        for u in range(n):
            if assignment[u] == -1:
                assignment[u] = omit
                
        cost, c_edges = evaluate_partition(assignment)
        if cost < best_cost:
            best_cost = cost
            best_edges = c_edges

    if best_cost <= B:
        print("YES")
        print(len(best_edges))
        for u, v in best_edges:
            print(f"{u} {v}")
        return

    # Branch and Bound for exact solution
    is_terminal = [-1] * n
    for i, t in enumerate(terminals):
        is_terminal[t] = i

    assignment = [-1] * n
    for i, t in enumerate(terminals):
        assignment[t] = i

    # Order non-terminal vertices by degree
    non_terminals = [u for u in range(n) if is_terminal[u] == -1]
    non_terminals.sort(key=lambda u: len(adj[u]), reverse=True)

    found_solution = [best_cost <= B]

    def bb(idx, current_cost):
        nonlocal best_cost, best_edges
        if current_cost >= best_cost or current_cost > B:
            return
        if idx == len(non_terminals):
            if current_cost < best_cost:
                best_cost = current_cost
                _, best_edges = evaluate_partition(assignment)
                if best_cost <= B:
                    found_solution[0] = True
            return

        u = non_terminals[idx]
        
        # Calculate cost additions for each label
        label_cost = [0] * k
        for v, w, _ in adj[u]:
            if assignment[v] != -1:
                for lbl in range(k):
                    if lbl != assignment[v]:
                        label_cost[lbl] += w

        # Try labels sorted by added cost
        sorted_labels = sorted(range(k), key=lambda lbl: label_cost[lbl])

        for lbl in sorted_labels:
            assignment[u] = lbl
            bb(idx + 1, current_cost + label_cost[lbl])
            assignment[u] = -1
            if found_solution[0]:
                return

    # Calculate base cost from terminal-terminal edges
    base_cost = 0
    for u, v, w, _ in edges:
        if is_terminal[u] != -1 and is_terminal[v] != -1 and is_terminal[u] != is_terminal[v]:
            base_cost += w

    bb(0, base_cost)

    if best_cost <= B:
        print("YES")
        print(len(best_edges))
        for u, v in best_edges:
            print(f"{u} {v}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()