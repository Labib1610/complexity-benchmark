import sys
import random

# Increase recursion depth just in case
sys.setrecursionlimit(100000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    idx = 2
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
        
    edge_color = [0] * m
    
    # Pre-allocate for speed
    def get_missing_colors(u):
        used = 0
        for e in adj[u]:
            c = edge_color[e]
            if c:
                used |= (1 << c)
        res = []
        if not (used & 2): res.append(1)
        if not (used & 4): res.append(2)
        if not (used & 8): res.append(3)
        return res

    def get_edge_with_color(u, c):
        for e in adj[u]:
            if edge_color[e] == c:
                return e
        return -1

    def solve_coloring():
        nonlocal edge_color
        edge_color = [0] * m
        
        # We will add edges one by one
        uncolored = list(range(m))
        random.shuffle(uncolored)
        
        step_count = 0
        max_steps = 100000
        
        while uncolored:
            e = uncolored.pop()
            curr_e = e
            
            while True:
                step_count += 1
                if step_count > max_steps:
                    return False
                
                u, v = edges[curr_e]
                mu = get_missing_colors(u)
                mv = get_missing_colors(v)
                
                common = [c for c in mu if c in mv]
                if common:
                    edge_color[curr_e] = random.choice(common)
                    break
                
                a = random.choice(mu)
                b = random.choice(mv)
                
                # Trace (a, b) alternating path from u
                path = []
                curr_node = u
                target_color = b # since 'a' is missing at u, first edge must have color b
                
                while True:
                    next_e = get_edge_with_color(curr_node, target_color)
                    if next_e == -1:
                        break
                    path.append(next_e)
                    u2, v2 = edges[next_e]
                    curr_node = v2 if curr_node == u2 else u2
                    target_color = a if target_color == b else b
                
                if curr_node != v:
                    # Path does not reach v! Flip colors on path
                    for pe in path:
                        edge_color[pe] = (a + b) - edge_color[pe]
                    edge_color[curr_e] = b
                    break
                else:
                    # Path reaches v. Kempe chain flip doesn't resolve directly.
                    # Pick a random color at u, uncolor that edge, and color curr_e with it.
                    colored_edges = [e_idx for e_idx in adj[u] if edge_color[e_idx] != 0]
                    if not colored_edges:
                        colored_edges = [e_idx for e_idx in adj[v] if edge_color[e_idx] != 0]
                    
                    chosen_e = random.choice(colored_edges)
                    c = edge_color[chosen_e]
                    edge_color[chosen_e] = 0
                    edge_color[curr_e] = c
                    curr_e = chosen_e
                    
        return True

    # Try running the heuristic with restarts
    for _ in range(5):
        if solve_coloring():
            print("YES")
            print(*(edge_color[i] for i in range(m)))
            return
            
    print("NO")

if __name__ == '__main__':
    solve()