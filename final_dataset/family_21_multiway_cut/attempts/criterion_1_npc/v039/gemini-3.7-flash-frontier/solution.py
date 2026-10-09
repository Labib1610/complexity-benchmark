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

    sources = [int(next(it)) for _ in range(k)]
    source_set = set(sources)

    edges = []
    adj_orig = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
        adj_orig[u].append((v, w, i))
        adj_orig[v].append((u, w, i))

    if k <= 1:
        print("YES")
        print(0)
        return

    # Dinic's Algorithm for max-flow / min-cut
    def get_min_cut(num_v, src, dst, graph_edges):
        # graph_edges: list of (u, v, cap)
        head = [-1] * num_v
        to = []
        cap = []
        nxt = []

        def add_edge(u, v, c):
            to.append(v)
            cap.append(c)
            nxt.append(head[u])
            head[u] = len(to) - 1

            to.append(u)
            cap.append(0)
            nxt.append(head[v])
            head[v] = len(to) - 1

        for u, v, c in graph_edges:
            add_edge(u, v, c)
            add_edge(v, u, c)

        level = [-1] * num_v

        def bfs():
            for i in range(num_v):
                level[i] = -1
            level[src] = 0
            q = deque([src])
            while q:
                u = q.popleft()
                e = head[u]
                while e != -1:
                    v = to[e]
                    if cap[e] > 0 and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
                    e = nxt[e]
            return level[dst] >= 0

        ptr = [0] * num_v

        def dfs(u, flow):
            if u == dst or flow == 0:
                return flow
            e = ptr[u]
            while e != -1:
                v = to[e]
                if level[v] == level[u] + 1 and cap[e] > 0:
                    pushed = dfs(v, min(flow, cap[e]))
                    if pushed > 0:
                        cap[e] -= pushed
                        cap[e ^ 1] += pushed
                        return pushed
                e = nxt[e]
                ptr[u] = e
            return 0

        max_flow = 0
        while bfs():
            for i in range(num_v):
                ptr[i] = head[i]
            while True:
                pushed = dfs(src, float('inf'))
                if pushed == 0:
                    break
                max_flow += pushed

        # Find reachable set from src
        visited = [False] * num_v
        q = deque([src])
        visited[src] = True
        while q:
            u = q.popleft()
            e = head[u]
            while e != -1:
                v = to[e]
                if cap[e] > 0 and not visited[v]:
                    visited[v] = True
                    q.append(v)
                e = nxt[e]

        return max_flow, visited

    # Heuristic / 2-approximation: isolating cuts
    # Graph vertices: 1..n, mapped to 0..n-1
    # For isolating cut of source s_i: source is s_i, sink is super-sink connected from all other sources with inf cap
    graph_edges = [(u - 1, v - 1, w) for u, v, w in edges]
    
    isolating_cuts = []
    for i, s in enumerate(sources):
        super_sink = n
        cur_edges = list(graph_edges)
        for j, s_other in enumerate(sources):
            if i != j:
                cur_edges.append((s_other - 1, super_sink, float('inf')))
        flow, reachable = get_min_cut(n + 1, s - 1, super_sink, cur_edges)
        isolating_cuts.append((flow, reachable, s))

    # Try 2-approx: union of isolating cuts except the maximum one
    isolating_cuts.sort(key=lambda x: x[0])
    
    # Assign terminals based on isolating cuts
    # If isolating cut i puts a vertex in S_i, assign it to S_i
    approx_assignment = [-1] * n
    for flow, reachable, s in isolating_cuts[:-1]:
        for v in range(n):
            if reachable[v] and approx_assignment[v] == -1:
                approx_assignment[v] = s
    worst_s = isolating_cuts[-1][2]
    for v in range(n):
        if approx_assignment[v] == -1:
            approx_assignment[v] = worst_s
    # Ensure source self-assignments
    for s in sources:
        approx_assignment[s - 1] = s

    def eval_cut(assignment):
        cut_edges = []
        cost = 0
        for u, v, w in edges:
            if assignment[u - 1] != assignment[v - 1]:
                cut_edges.append((u, v))
                cost += w
        return cost, cut_edges

    best_cost, best_cut = eval_cut(approx_assignment)

    if best_cost <= B:
        print("YES")
        print(len(best_cut))
        for u, v in best_cut:
            print(f"{u} {v}")
        return

    # If 2-approx > B, use Branch and Bound
    # Map sources to 0..k-1
    s_map = {s: i for i, s in enumerate(sources)}
    initial_assignment = [-1] * n
    for s in sources:
        initial_assignment[s - 1] = s_map[s]

    best_solution = [best_cost, best_cut]

    # Order non-terminal vertices by degree / max incident weight to terminals
    non_terminals = [v for v in range(n) if (v + 1) not in source_set]
    non_terminals.sort(key=lambda v: sum(w for to_v, w, _ in adj_orig[v + 1]), reverse=True)

    def branch(idx, current_assignment):
        if idx == len(non_terminals):
            full_assignment = [sources[current_assignment[v]] for v in range(n)]
            cost, cut = eval_cut(full_assignment)
            if cost < best_solution[0]:
                best_solution[0] = cost
                best_solution[1] = cut
            return

        # Lower bound calculation
        # Sum of min-cuts between each terminal group and others
        # Contract already assigned vertices to terminal super-nodes
        terminal_nodes = [[] for _ in range(k)]
        for v in range(n):
            if current_assignment[v] != -1:
                terminal_nodes[current_assignment[v]].append(v)

        # Quick lower bound
        lb_sum = 0
        super_sink = n
        for t in range(k):
            # source is terminal t, sink is super_sink
            cur_edges = []
            for u, v, w in edges:
                cur_edges.append((u - 1, v - 1, w))
            # connect all other assigned vertices to super_sink
            for other_t in range(k):
                if other_t != t:
                    for v in terminal_nodes[other_t]:
                        cur_edges.append((v, super_sink, float('inf')))
            src = terminal_nodes[t][0]
            for v in terminal_nodes[t][1:]:
                cur_edges.append((src, v, float('inf')))
            flow, _ = get_min_cut(n + 1, src, super_sink, cur_edges)
            lb_sum += flow

        lb = (lb_sum + 1) // 2
        if lb >= best_solution[0]:
            return

        v = non_terminals[idx]
        # Try assigning v to terminals ordered by connection strength
        weights_to_t = [0] * k
        for to_v, w, _ in adj_orig[v + 1]:
            t_assigned = current_assignment[to_v - 1]
            if t_assigned != -1:
                weights_to_t[t_assigned] += w

        order = sorted(range(k), key=lambda t: weights_to_t[t], reverse=True)

        for t in order:
            current_assignment[v] = t
            branch(idx + 1, current_assignment)
            current_assignment[v] = -1
            if best_solution[0] <= B:
                # Early exit if we just need <= B
                pass

    branch(0, initial_assignment)

    if best_solution[0] <= B:
        print("YES")
        print(len(best_solution[1]))
        for u, v in best_solution[1]:
            print(f"{u} {v}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()