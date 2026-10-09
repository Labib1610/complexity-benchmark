import sys

# Increase recursion depth for deep search trees
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    n = int(next(iterator))
    m = int(next(iterator))
    k = int(next(iterator))
    B = int(next(iterator))
    
    sources = [int(next(iterator)) - 1 for _ in range(k)]
    
    adj = [[] for _ in range(n)]
    edges = []
    
    for i in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        w = int(next(iterator))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
        
    labels = [-1] * n
    for i, s in enumerate(sources):
        labels[s] = i
        
    unassigned = [v for v in range(n) if labels[v] == -1]
    
    inc = [[0] * k for _ in range(n)]
    total = [0] * n
    max_inc = [0] * n
    cost_extra = [0] * n
    
    for v in unassigned:
        for u, w in adj[v]:
            if labels[u] != -1:
                lbl = labels[u]
                inc[v][lbl] += w
                total[v] += w
        m_inc = 0
        for l in range(k):
            if inc[v][l] > m_inc:
                m_inc = inc[v][l]
        max_inc[v] = m_inc
        cost_extra[v] = total[v] - m_inc

    initial_cost = 0
    for u, v, w in edges:
        if labels[u] != -1 and labels[v] != -1:
            if labels[u] != labels[v]:
                initial_cost += w

    if initial_cost > B:
        print("NO")
        return

    sum_cost_extra = sum(cost_extra[v] for v in unassigned)
    
    unassigned_set = set(unassigned)
    
    solution_labels = None

    def search(current_cost, current_sum_extra):
        nonlocal solution_labels
        if solution_labels is not None:
            return True

        if not unassigned_set:
            if current_cost <= B:
                solution_labels = list(labels)
                return True
            return False

        # Pick the most constrained unassigned vertex (max total or max_inc)
        best_v = -1
        best_val = -1
        for v in unassigned_set:
            if total[v] > best_val:
                best_val = total[v]
                best_v = v

        # If all remaining unassigned vertices have total == 0,
        # they are not adjacent to any assigned vertex.
        # We can safely assign them all to label 0 with 0 extra cost.
        if best_val == 0:
            if current_cost <= B:
                for v in unassigned_set:
                    labels[v] = 0
                solution_labels = list(labels)
                return True
            return False

        v = best_v
        unassigned_set.remove(v)
        old_cost_extra_v = cost_extra[v]
        
        # Try labels sorted by inc[v][l] descending
        label_order = sorted(range(k), key=lambda l: inc[v][l], reverse=True)
        
        for l in label_order:
            edge_cut_cost = total[v] - inc[v][l]
            new_cost = current_cost + edge_cut_cost
            
            # Predict updates to neighbors
            delta_extra = 0
            history = []
            
            for u, w in adj[v]:
                if u in unassigned_set:
                    old_c_u = cost_extra[u]
                    old_tot_u = total[u]
                    old_inc_u_l = inc[u][l]
                    old_max_inc_u = max_inc[u]
                    
                    new_inc_u_l = old_inc_u_l + w
                    new_tot_u = old_tot_u + w
                    new_max_inc_u = max(old_max_inc_u, new_inc_u_l)
                    new_c_u = new_tot_u - new_max_inc_u
                    
                    delta_extra += (new_c_u - old_c_u)
                    history.append((u, old_tot_u, old_inc_u_l, old_max_inc_u, old_c_u))

            new_sum_extra = current_sum_extra - old_cost_extra_v + delta_extra
            
            if new_cost + new_sum_extra <= B:
                # Apply changes
                labels[v] = l
                for u, old_tot_u, old_inc_u_l, old_max_inc_u, old_c_u in history:
                    w_edge = old_tot_u # we know w is difference
                    # Reapply efficiently
                    pass
                for u, w in adj[v]:
                    if u in unassigned_set:
                        inc[u][l] += w
                        total[u] += w
                        if inc[u][l] > max_inc[u]:
                            max_inc[u] = inc[u][l]
                        cost_extra[u] = total[u] - max_inc[u]
                        
                if search(new_cost, new_sum_extra):
                    return True
                
                # Rollback neighbor changes
                labels[v] = -1
                for u, old_tot_u, old_inc_u_l, old_max_inc_u, old_c_u in history:
                    total[u] = old_tot_u
                    inc[u][l] = old_inc_u_l
                    max_inc[u] = old_max_inc_u
                    cost_extra[u] = old_c_u

        unassigned_set.add(v)
        return False

    if search(initial_cost, sum_cost_extra):
        print("YES")
        cut_edges = []
        for u, v, w in edges:
            if solution_labels[u] != solution_labels[v]:
                cut_edges.append((u + 1, v + 1))
        print(len(cut_edges))
        for u, v in cut_edges:
            print(f"{u} {v}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()