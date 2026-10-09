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
    
    commodities = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        commodities.append((s, t, d))
        
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))
        adj[u].append((v, i))

    res_cap = [edges[i][2] for i in range(m)]
    flow = [[0] * m for _ in range(k)]
    rem = [commodities[i][2] for i in range(k)]

    def find_path(s, t):
        parent = [-1] * n
        parent_edge = [-1] * n
        queue = deque([s])
        parent[s] = s
        while queue:
            u = queue.popleft()
            if u == t:
                break
            for v, e_idx in adj[u]:
                if parent[v] == -1 and res_cap[e_idx] > 0:
                    parent[v] = u
                    parent_edge[v] = e_idx
                    queue.append(v)
        
        if parent[t] == -1:
            return None, 0
        
        path_edges = []
        curr = t
        bot = float('inf')
        while curr != s:
            e_idx = parent_edge[curr]
            path_edges.append(e_idx)
            bot = min(bot, res_cap[e_idx])
            curr = parent[curr]
        path_edges.reverse()
        return path_edges, bot

    import time
    start_time = time.time()

    def search(c_idx):
        if time.time() - start_time > 4.5:
            return False
        
        # Find next commodity with remaining demand
        while c_idx < k and rem[c_idx] == 0:
            c_idx += 1
            
        if c_idx == k:
            return True

        s, t, _ = commodities[c_idx]
        
        # Try finding paths until this commodity is satisfied
        path, bot = find_path(s, t)
        if not path:
            return False
            
        push = min(bot, rem[c_idx])
        
        # Apply push
        for e in path:
            res_cap[e] -= push
            flow[c_idx][e] += push
        rem[c_idx] -= push
        
        if search(c_idx):
            return True
            
        # Backtrack
        for e in path:
            res_cap[e] += push
            flow[c_idx][e] -= push
        rem[c_idx] += push
        
        # Also try pushing smaller amounts (unit flow) if push > 1
        if push > 1:
            push = 1
            for e in path:
                res_cap[e] -= push
                flow[c_idx][e] += push
            rem[c_idx] -= push
            
            if search(c_idx):
                return True
                
            for e in path:
                res_cap[e] += push
                flow[c_idx][e] -= push
            rem[c_idx] += push

        return False

    if search(0):
        print("YES")
        for i in range(k):
            print(*(flow[i]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()