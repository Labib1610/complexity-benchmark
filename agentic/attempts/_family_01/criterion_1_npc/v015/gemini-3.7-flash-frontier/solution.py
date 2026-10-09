import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    adj_mask = [0] * n
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u != v:
            adj[u].append(v)
            adj[v].append(u)
            adj_mask[u] |= (1 << v)
            adj_mask[v] |= (1 << u)

    # State for each vertex:
    # 0: unassigned
    # 1: in I (color 1)
    # 2: in V \ I (color 2 or 3)
    state = [0] * n

    def is_bipartite_compatible(v_not_in_I_list):
        # Check if the subgraph induced by vertices with state == 2 is bipartite
        color_2sat = {}
        for v in v_not_in_I_list:
            if v not in color_2sat:
                color_2sat[v] = 2
                queue = [v]
                while queue:
                    curr = queue.pop(0)
                    curr_c = color_2sat[curr]
                    next_c = 3 if curr_c == 2 else 2
                    for neighbor in adj[curr]:
                        if state[neighbor] == 2:
                            if neighbor in color_2sat:
                                if color_2sat[neighbor] != next_c:
                                    return False, None
                            else:
                                color_2sat[neighbor] = next_c
                                queue.append(neighbor)
        return True, color_2sat

    def get_full_2coloring(v_not_in_I_list):
        # 2-color all vertices in V \ I
        color_map = {}
        for v in v_not_in_I_list:
            if v not in color_map:
                color_map[v] = 2
                queue = [v]
                while queue:
                    curr = queue.pop(0)
                    curr_c = color_map[curr]
                    next_c = 3 if curr_c == 2 else 2
                    for neighbor in adj[curr]:
                        if state[neighbor] == 2:
                            if neighbor in color_map:
                                if color_map[neighbor] != next_c:
                                    return None
                            else:
                                color_map[neighbor] = next_c
                                queue.append(neighbor)
        return color_map

    def backtrack():
        # Find unassigned vertex with max degree among remaining unassigned
        best_v = -1
        max_deg = -1
        for i in range(n):
            if state[i] == 0:
                deg = sum(1 for neighbor in adj[i] if state[neighbor] == 0)
                if deg > max_deg:
                    max_deg = deg
                    best_v = i
        
        if best_v == -1:
            # All vertices assigned, verify if V \ I is bipartite
            v_not_in_I = [i for i in range(n) if state[i] == 2]
            color_map = get_full_2coloring(v_not_in_I)
            if color_map is not None:
                ans = [0] * n
                for i in range(n):
                    if state[i] == 1:
                        ans[i] = 1
                    else:
                        ans[i] = color_map[i]
                return ans
            return None

        # Branch 1: Put best_v in I (color 1)
        # All neighbors must go to V \ I (state = 2)
        changed = [best_v]
        state[best_v] = 1
        valid = True
        for neighbor in adj[best_v]:
            if state[neighbor] == 1:
                valid = False
                break
            if state[neighbor] == 0:
                state[neighbor] = 2
                changed.append(neighbor)
        
        if valid:
            v_not_in_I = [i for i in range(n) if state[i] == 2]
            ok, _ = is_bipartite_compatible(v_not_in_I)
            if ok:
                res = backtrack()
                if res is not None:
                    return res
        
        # Backtrack Branch 1
        for u in changed:
            state[u] = 0

        # Branch 2: Exclude best_v from I (state = 2)
        state[best_v] = 2
        v_not_in_I = [i for i in range(n) if state[i] == 2]
        ok, _ = is_bipartite_compatible(v_not_in_I)
        if ok:
            res = backtrack()
            if res is not None:
                return res
        
        # Backtrack Branch 2
        state[best_v] = 0
        return None

    res = backtrack()
    if res is not None:
        print("YES")
        print(*(res[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()