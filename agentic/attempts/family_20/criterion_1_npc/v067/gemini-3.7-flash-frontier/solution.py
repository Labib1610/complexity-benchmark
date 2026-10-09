import sys
import random
import time

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    edge_color = [0] * m
    # color_edge[u][c] = edge index incident to u with color c (1, 2, or 3), or -1
    color_edge = [[-1] * 4 for _ in range(n + 1)]

    def get_missing_color(u):
        for c in (1, 2, 3):
            if color_edge[u][c] == -1:
                return c
        return -1

    def flip_kempe(start_u, c1, c2):
        # Flips the (c1, c2) alternating path starting at start_u
        curr = start_u
        c = c1 if color_edge[start_u][c1] != -1 else c2
        path_edges = []
        while True:
            e = color_edge[curr][c]
            if e == -1:
                break
            path_edges.append((e, curr, c))
            u, v = edges[e]
            curr = v if curr == u else u
            c = c2 if c == c1 else c1
        
        for e, u, old_c in path_edges:
            new_c = c2 if old_c == c1 else c1
            v = edges[e][1] if edges[e][0] == u else edges[e][0]
            color_edge[u][old_c] = -1
            color_edge[v][old_c] = -1
            edge_color[e] = new_c
            color_edge[u][new_c] = e
            color_edge[v][new_c] = e
        return curr  # end vertex of the path

    start_time = time.time()
    
    # Try multiple restarts if needed
    for restart in range(10):
        if time.time() - start_time > 4.2:
            break
            
        edge_color = [0] * m
        color_edge = [[-1] * 4 for _ in range(n + 1)]
        
        uncolored = list(range(m))
        random.shuffle(uncolored)
        
        success = True
        while uncolored:
            if time.time() - start_time > 4.2:
                success = False
                break
                
            e = uncolored.pop()
            u, v = edges[e]
            
            c_u = get_missing_color(u)
            c_v = get_missing_color(v)
            
            if c_u == c_v:
                edge_color[e] = c_u
                color_edge[u][c_u] = e
                color_edge[v][c_u] = e
                continue
            
            # Step limit for coloring this edge
            step = 0
            colored_e = False
            while step < 100:
                step += 1
                c_u = get_missing_color(u)
                c_v = get_missing_color(v)
                
                if c_u == c_v:
                    edge_color[e] = c_u
                    color_edge[u][c_u] = e
                    color_edge[v][c_u] = e
                    colored_e = True
                    break
                
                # Check (c_u, c_v) alternating path from u
                end_node = flip_kempe(u, c_u, c_v)
                if end_node != v:
                    # Path did not end at v, now c_v is missing at both u and v
                    edge_color[e] = c_v
                    color_edge[u][c_v] = e
                    color_edge[v][c_v] = e
                    colored_e = True
                    break
                else:
                    # Path ended at v, flip it back
                    flip_kempe(u, c_u, c_v)
                    
                    # Choose a different color at u to perturb
                    # Colors at u are c_v and c_other
                    c_other = 6 - c_u - c_v
                    if random.random() < 0.5:
                        flip_kempe(u, c_u, c_other)
                    else:
                        flip_kempe(v, c_v, c_other)
            
            if not colored_e:
                # If stuck, uncolor a random incident edge and retry
                incident = [ei for ei in adj[u] + adj[v] if edge_color[ei] != 0]
                if incident:
                    e_drop = random.choice(incident)
                    c_drop = edge_color[e_drop]
                    du, dv = edges[e_drop]
                    color_edge[du][c_drop] = -1
                    color_edge[dv][c_drop] = -1
                    edge_color[e_drop] = 0
                    uncolored.append(e_drop)
                uncolored.append(e)
                random.shuffle(uncolored)

        if all(edge_color[i] != 0 for i in range(m)):
            print("YES")
            print(*(edge_color[i] for i in range(m)))
            return

    print("NO")

if __name__ == '__main__':
    solve()