import sys
import time
import random
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    B = int(input_data[2])
    
    if n == 1:
        if B >= 0:
            print("YES")
            print("1")
        else:
            print("NO")
        return

    adj = [[] for _ in range(n + 1)]
    edges = []
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
        idx += 2
        
    start_time = time.time()
    time_limit = 4.7  # seconds

    def compute_cost(pos):
        c = 0
        for u, v in edges:
            c += abs(pos[u] - pos[v])
        return c

    best_cost = float('inf')
    best_pos = None

    def check_solution(pos):
        nonlocal best_cost, best_pos
        c = compute_cost(pos)
        if c < best_cost:
            best_cost = c
            best_pos = list(pos)
        return c <= B

    # Heuristic 1: Centroid layout
    # Find tree sizes
    sz = [0] * (n + 1)
    def get_sizes(u, p):
        s = 1
        for v in adj[u]:
            if v != p:
                s += get_sizes(v, u)
        sz[u] = s
        return s

    def get_centroid(u, p, total):
        for v in adj[u]:
            if v != p and sz[v] > total // 2:
                return get_centroid(v, u, total)
        return u

    get_sizes(1, 0)
    centroid = get_centroid(1, 0, n)

    # Recursive layout
    def layout_tree(root):
        # returns list of nodes in layout order
        def dfs(u, p):
            children = [v for v in adj[u] if v != p]
            # sort children by subtree size descending
            children.sort(key=lambda x: sz[x], reverse=True)
            left = []
            right = []
            for i, v in enumerate(children):
                sub = dfs(v, u)
                if i % 2 == 0:
                    left.extend(sub)
                else:
                    right.extend(sub)
            return left + [u] + right
        get_sizes(root, 0)
        return dfs(root, 0)

    # Try layout from centroid and some other roots
    roots_to_try = [centroid, 1]
    if n > 2:
        # add a few random roots
        roots_to_try.extend(random.sample(range(1, n + 1), min(n, 10)))

    for r in set(roots_to_try):
        order = layout_tree(r)
        pos = [0] * (n + 1)
        for i, node in enumerate(order):
            pos[node] = i + 1
        if check_solution(pos):
            print("YES")
            print(*(best_pos[1:]))
            return

    # Heuristic 2: DFS orders with different rootings
    for r in set(roots_to_try):
        order = []
        visited = [False] * (n + 1)
        stack = [r]
        visited[r] = True
        while stack:
            u = stack.pop()
            order.append(u)
            # sort neighbors by degree
            neighbors = [v for v in adj[u] if not visited[v]]
            neighbors.sort(key=lambda x: len(adj[x]))
            for v in neighbors:
                visited[v] = True
                stack.append(v)
        pos = [0] * (n + 1)
        for i, node in enumerate(order):
            pos[node] = i + 1
        if check_solution(pos):
            print("YES")
            print(*(best_pos[1:]))
            return

    # Simulated Annealing / Local Search starting from best_pos
    pos = list(best_pos)
    # inv_pos[p] = node at position p
    inv_pos = [0] * (n + 1)
    for i in range(1, n + 1):
        inv_pos[pos[i]] = i

    cur_cost = best_cost
    T = max(1.0, float(cur_cost) * 0.1)
    cooling_rate = 0.99995

    # Fast swap delta calculation
    # When swapping nodes u and v:
    # delta = new_cost - old_cost
    def get_swap_delta(u, v):
        pu, pv = pos[u], pos[v]
        delta = 0
        for w in adj[u]:
            if w == v:
                continue
            delta += abs(pv - pos[w]) - abs(pu - pos[w])
        for w in adj[v]:
            if w == u:
                continue
            delta += abs(pu - pos[w]) - abs(pv - pos[w])
        return delta

    iter_count = 0
    while time.time() - start_time < time_limit:
        iter_count += 1
        if iter_count % 1000 == 0:
            if best_cost <= B:
                print("YES")
                print(*(best_pos[1:]))
                return

        # Pick two nodes to swap
        if random.random() < 0.7:
            # swap two nodes close in position or connected by an edge
            if random.random() < 0.5:
                p1 = random.randint(1, n)
                p2 = max(1, min(n, p1 + random.choice([-2, -1, 1, 2])))
                if p1 == p2:
                    continue
                u = inv_pos[p1]
                v = inv_pos[p2]
            else:
                u, v = random.choice(edges)
        else:
            u = random.randint(1, n)
            v = random.randint(1, n)
            if u == v:
                continue

        delta = get_swap_delta(u, v)

        if delta < 0 or (T > 1e-6 and math.exp(-delta / T) > random.random()):
            cur_cost += delta
            p_u, p_v = pos[u], pos[v]
            pos[u], pos[v] = p_v, p_u
            inv_pos[p_u], inv_pos[p_v] = v, u

            if cur_cost < best_cost:
                best_cost = cur_cost
                best_pos = list(pos)
                if best_cost <= B:
                    print("YES")
                    print(*(best_pos[1:]))
                    return

        T *= cooling_rate
        if T < 1e-4:
            T = max(1.0, float(cur_cost) * 0.05)

    if best_cost <= B:
        print("YES")
        print(*(best_pos[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()