import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    T = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    radj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        adj[a].append(b)
        radj[b].append(a)
    
    # Topological sort with cycle detection
    visited = [0] * (n + 1)  # 0=unvisited, 1=in progress, 2=done
    order = []
    has_cycle = [False]
    
    def dfs(u):
        visited[u] = 1
        for v in adj[u]:
            if visited[v] == 1:
                has_cycle[0] = True
                return
            elif visited[v] == 0:
                dfs(v)
                if has_cycle[0]:
                    return
        visited[u] = 2
        order.append(u)
    
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)
            if has_cycle[0]:
                print("NO")
                return
    
    order.reverse()
    
    # Compute earliest cycle for each node (longest path + 1)
    earliest = [0] * (n + 1)
    for u in order:
        e = 1
        for p in radj[u]:
            if earliest[p] + 1 > e:
                e = earliest[p] + 1
        earliest[u] = e
        if e > T:
            print("NO")
            return
    
    # Segment tree to find earliest slot with count < M
    # Size T+2 (1-indexed, positions 1..T)
    size = 1
    while size < T + 2:
        size *= 2
    seg = [0] * (2 * size)
    
    def update(pos):
        pos += size
        seg[pos] += 1
        pos //= 2
        while pos >= 1:
            seg[pos] = seg[2*pos] + seg[2*pos+1]
            pos //= 2
    
    def query_first_under_M(l, r):
        # Find first position in [l, r] with value < M
        # Returns -1 if none
        l += size
        r += size
        # Collect nodes
        left_nodes = []
        right_nodes = []
        while l <= r:
            if l & 1:
                left_nodes.append(l)
                l += 1
            if not (r & 1):
                right_nodes.append(r)
                r -= 1
            l //= 2
            r //= 2
        nodes = left_nodes + right_nodes[::-1]
        for node in nodes:
            if seg[node] < M:
                # Descend to find leftmost
                while node < size:
                    if seg[2*node] < M:
                        node = 2*node
                    else:
                        node = 2*node + 1
                return node - size
        return -1
    
    assign = [0] * (n + 1)
    for u in order:
        e = earliest[u]
        pos = query_first_under_M(e, T)
        if pos == -1:
            print("NO")
            return
        assign[u] = pos
        update(pos)
    
    print("YES")
    print(' '.join(str(assign[i]) for i in range(1, n + 1)))

solve()