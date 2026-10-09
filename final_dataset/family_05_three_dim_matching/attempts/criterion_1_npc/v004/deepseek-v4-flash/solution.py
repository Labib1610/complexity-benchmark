import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    allowed = set()
    xy_allowed = [[False]*(k+1) for _ in range(k+1)]
    yz_allowed = [[False]*(k+1) for _ in range(k+1)]
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        allowed.add((x, y, z))
        xy_allowed[x][y] = True
        yz_allowed[y][z] = True
    
    # Build flow network for X -> Y
    # Nodes: source=0, X:1..k, Y:k+1..2k, sink=2k+1
    N = 2*k + 2
    graph = [[] for _ in range(N)]
    
    def add_edge(u, v, cap):
        graph[u].append([v, cap, len(graph[v])])
        graph[v].append([u, 0, len(graph[u])-1])
    
    S = 0
    T = 2*k + 1
    for x in range(1, k+1):
        add_edge(S, x, 1)
    for y in range(1, k+1):
        add_edge(k+y, T, 1)
    for x in range(1, k+1):
        for y in range(1, k+1):
            if xy_allowed[x][y]:
                add_edge(x, k+y, 1)
    
    # Dinic
    def bfs():
        level = [-1]*N
        q = deque([S])
        level[S] = 0
        while q:
            u = q.popleft()
            for v, cap, rev in graph[u]:
                if cap > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level
    
    def dfs(u, f, level, it_ptr):
        if u == T:
            return f
        while it_ptr[u] < len(graph[u]):
            v, cap, rev = graph[u][it_ptr[u]]
            if cap > 0 and level[v] == level[u] + 1:
                ret = dfs(v, min(f, cap), level, it_ptr)
                if ret > 0:
                    graph[u][it_ptr[u]][1] -= ret
                    graph[v][rev][1] += ret
                    return ret
            it_ptr[u] += 1
        return 0
    
    flow = 0
    while True:
        level = bfs()
        if level[T] == -1:
            break
        it_ptr = [0]*N
        while True:
            f = dfs(S, 10**9, level, it_ptr)
            if f == 0:
                break
            flow += f
    
    if flow != k:
        print("NO")
        return
    
    # Reconstruct X-Y matching
    xy_match = [0]*(k+1)  # x -> y
    yx_match = [0]*(k+1)  # y -> x
    for x in range(1, k+1):
        for v, cap, rev in graph[x]:
            if 1 <= v-k <= k and cap == 0:  # edge used
                y = v - k
                xy_match[x] = y
                yx_match[y] = x
    
    # Now assign z for each (x,y)
    used_z = [False]*(k+1)
    result = []
    for x in range(1, k+1):
        y = xy_match[x]
        found = False
        for z in range(1, k+1):
            if not used_z[z] and (x, y, z) in allowed:
                used_z[z] = True
                result.append((x, y, z))
                found = True
                break
        if not found:
            print("NO")
            return
    
    print("YES")
    for x, y, z in result:
        print(x, y, z)

if __name__ == "__main__":
    solve()