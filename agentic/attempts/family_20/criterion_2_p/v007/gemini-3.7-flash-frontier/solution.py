import sys
import random

# Increase recursion depth just in case
sys.setrecursionlimit(1000000)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    nL = int(input_data[0])
    nR = int(input_data[1])
    m = int(input_data[2])
    
    if m == 0:
        print("YES")
        print()
        return

    edges_raw = []
    deg_L = [0] * nL
    deg_R = [0] * nR
    
    idx = 3
    for i in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        edges_raw.append((u, v))
        deg_L[u] += 1
        deg_R[v] += 1
        
    Delta = max(max(deg_L), max(deg_R))
    if Delta == 0:
        print("YES")
        print()
        return

    # Step 1: Greedy bin packing of vertices into super-nodes of capacity Delta
    L_map = [0] * nL
    curr_deg = 0
    curr_super = 0
    for u in range(nL):
        if deg_L[u] == 0:
            continue
        if curr_deg + deg_L[u] <= Delta:
            L_map[u] = curr_super
            curr_deg += deg_L[u]
        else:
            curr_super += 1
            L_map[u] = curr_super
            curr_deg = deg_L[u]
    B_L = curr_super + 1 if any(d > 0 for d in deg_L) else 0

    R_map = [0] * nR
    curr_deg = 0
    curr_super = 0
    for v in range(nR):
        if deg_R[v] == 0:
            continue
        if curr_deg + deg_R[v] <= Delta:
            R_map[v] = curr_super
            curr_deg += deg_R[v]
        else:
            curr_super += 1
            R_map[v] = curr_super
            curr_deg = deg_R[v]
    B_R = curr_super + 1 if any(d > 0 for d in deg_R) else 0

    B = max(B_L, B_R, 1)

    # Step 2: Build regularized multigraph
    super_deg_L = [0] * B
    super_deg_R = [0] * B
    edges = []
    for i in range(m):
        u, v = edges_raw[i]
        su = L_map[u]
        sv = R_map[v]
        edges.append((su, sv, i))
        super_deg_L[su] += 1
        super_deg_R[sv] += 1

    # Add dummy edges to make every node have degree exactly Delta
    p_L = 0
    p_R = 0
    while p_L < B and p_R < B:
        while p_L < B and super_deg_L[p_L] == Delta:
            p_L += 1
        while p_R < B and super_deg_R[p_R] == Delta:
            p_R += 1
        if p_L == B or p_R == B:
            break
        add_count = min(Delta - super_deg_L[p_L], Delta - super_deg_R[p_R])
        for _ in range(add_count):
            edges.append((p_L, p_R, -1))
        super_deg_L[p_L] += add_count
        super_deg_R[p_R] += add_count

    ans = [0] * m

    # Step 3: Divide and Conquer Coloring
    def solve(cur_edges, d, color_offset):
        if d == 0:
            return
        if d == 1:
            for u, v, orig_id in cur_edges:
                if orig_id != -1:
                    ans[orig_id] = color_offset
            return

        if d % 2 == 1:
            # Find a 1-factor using random walk alternating paths
            adj_L = [[] for _ in range(B)]
            for edge in cur_edges:
                u, v, orig_id = edge
                adj_L[u].append(edge)

            match_L = [-1] * B
            match_R = [-1] * B
            match_edge_L = [None] * B

            for s in range(B):
                if match_L[s] != -1:
                    continue
                curr = s
                stack_u = [s]
                stack_v = []
                pos_in_stack = {s: 0}

                while True:
                    edge = random.choice(adj_L[curr])
                    v = edge[1]

                    if match_R[v] == -1:
                        stack_v.append((v, edge))
                        for i in range(len(stack_v)):
                            ui = stack_u[i]
                            vi, ei = stack_v[i]
                            match_L[ui] = vi
                            match_R[vi] = ui
                            match_edge_L[ui] = ei
                        break
                    else:
                        u_prime = match_R[v]
                        if u_prime in pos_in_stack:
                            idx = pos_in_stack[u_prime]
                            for popped_u in stack_u[idx + 1:]:
                                del pos_in_stack[popped_u]
                            stack_u = stack_u[:idx + 1]
                            stack_v = stack_v[:idx]
                            curr = u_prime
                        else:
                            stack_v.append((v, edge))
                            stack_u.append(u_prime)
                            pos_in_stack[u_prime] = len(stack_u) - 1
                            curr = u_prime

            # Extract 1-factor and color it
            matched_set = set(id(e) for e in match_edge_L)
            edges_remaining = []
            for e in cur_edges:
                if id(e) in matched_set:
                    matched_set.remove(id(e))
                    if e[2] != -1:
                        ans[e[2]] = color_offset
                else:
                    edges_remaining.append(e)

            solve(edges_remaining, d - 1, color_offset + 1)
        else:
            # d is even: Eulerian circuit decomposition
            adj = [[] for _ in range(2 * B)]
            for eid, (u, v, orig_id) in enumerate(cur_edges):
                adj[u].append((v + B, eid))
                adj[v + B].append((u, eid))

            used = [False] * len(cur_edges)
            head = [0] * (2 * B)
            edges1 = []
            edges2 = []

            for start in range(2 * B):
                if head[start] == len(adj[start]):
                    continue
                stack = [(start, None)]
                comp_edges = []
                while stack:
                    u, in_edge = stack[-1]
                    while head[u] < len(adj[u]) and used[adj[u][head[u]][1]]:
                        head[u] += 1
                    if head[u] < len(adj[u]):
                        v, eid = adj[u][head[u]]
                        head[u] += 1
                        used[eid] = True
                        stack.append((v, eid))
                    else:
                        stack.pop()
                        if in_edge is not None:
                            comp_edges.append(in_edge)

                for i in range(len(comp_edges)):
                    if i % 2 == 0:
                        edges1.append(cur_edges[comp_edges[i]])
                    else:
                        edges2.append(cur_edges[comp_edges[i]])

            half = d // 2
            solve(edges1, half, color_offset)
            solve(edges2, half, color_offset + half)

    solve(edges, Delta, 1)

    print("YES")
    print(*(ans[i] for i in range(m)))

if __name__ == '__main__':
    main()