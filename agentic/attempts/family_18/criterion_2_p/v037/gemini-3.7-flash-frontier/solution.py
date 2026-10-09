import sys
import time

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        
    start_time = time.time()
    
    def get_tree_layout(root):
        visited = [False] * (n + 1)
        parent = [0] * (n + 1)
        order = []
        stack = [root]
        visited[root] = True
        
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)
                    
        subtree_size = [1] * (n + 1)
        for u in reversed(order):
            if parent[u] != 0:
                subtree_size[parent[u]] += subtree_size[u]
                
        layouts = [None] * (n + 1)
        root_idx = [0] * (n + 1)
        
        for u in reversed(order):
            children = [v for v in adj[u] if v != parent[u]]
            if not children:
                layouts[u] = [u]
                root_idx[u] = 0
                continue
            
            children.sort(key=lambda v: subtree_size[v])
            
            left_children = []
            right_children = []
            for i, c in enumerate(children):
                if i % 2 == 0:
                    right_children.append(c)
                else:
                    left_children.append(c)
                    
            left_part = []
            for c in reversed(left_children):
                c_layout = layouts[c]
                c_pos = root_idx[c]
                sz = len(c_layout)
                if c_pos < sz - 1 - c_pos:
                    c_layout.reverse()
                    c_pos = sz - 1 - c_pos
                left_part.extend(c_layout)
                
            right_part = []
            for c in right_children:
                c_layout = layouts[c]
                c_pos = root_idx[c]
                sz = len(c_layout)
                if c_pos > sz - 1 - c_pos:
                    c_layout.reverse()
                    c_pos = sz - 1 - c_pos
                right_part.extend(c_layout)
                
            u_layout = left_part + [u] + right_part
            layouts[u] = u_layout
            root_idx[u] = len(left_part)
            
        return layouts[root]

    def compute_cost(pos):
        cost = 0
        for u, v in edges:
            cost += abs(pos[u] - pos[v])
        return cost

    best_cost = float('inf')
    best_pos = None
    
    roots_to_try = list(range(1, n + 1))
    if n > 500:
        deg = [(len(adj[i]), i) for i in range(1, n + 1)]
        deg.sort(reverse=True)
        roots_to_try = [x[1] for x in deg[:100]] + list(range(1, min(n + 1, 50)))
        roots_to_try = list(dict.fromkeys(roots_to_try))
    
    for r in roots_to_try:
        layout = get_tree_layout(r)
        pos = [0] * (n + 1)
        for i, u in enumerate(layout):
            pos[u] = i + 1
            
        cost = compute_cost(pos)
        if cost < best_cost:
            best_cost = cost
            best_pos = pos
            if best_cost <= B:
                break

    if best_cost <= B:
        print("YES")
        print(*(best_pos[1:]))
        return

    # Local search (adjacent swap / simulated annealing)
    curr_pos = list(best_pos)
    arr = [0] * n
    for i in range(1, n + 1):
        arr[curr_pos[i] - 1] = i
    curr_cost = best_cost

    import random
    steps = 0
    while time.time() - start_time < 4.5:
        steps += 1
        i = random.randint(0, n - 2)
        u, v = arr[i], arr[i + 1]
        
        diff = 0
        for nb in adj[u]:
            if nb != v:
                diff += abs(curr_pos[u] + 1 - curr_pos[nb]) - abs(curr_pos[u] - curr_pos[nb])
        for nb in adj[v]:
            if nb != u:
                diff += abs(curr_pos[v] - 1 - curr_pos[nb]) - abs(curr_pos[v] - curr_pos[nb])
                
        if diff <= 0:
            arr[i], arr[i + 1] = v, u
            curr_pos[u] += 1
            curr_pos[v] -= 1
            curr_cost += diff
            if curr_cost < best_cost:
                best_cost = curr_cost
                best_pos = list(curr_pos)
                if best_cost <= B:
                    break
        else:
            if random.random() < 0.005:
                arr[i], arr[i + 1] = v, u
                curr_pos[u] += 1
                curr_pos[v] -= 1
                curr_cost += diff

    if best_cost <= B:
        print("YES")
        print(*(best_pos[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()