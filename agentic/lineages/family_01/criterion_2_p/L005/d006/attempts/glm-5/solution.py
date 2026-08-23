import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    parent = [0] * (n + 1)
    order = []
    
    for start in range(1, n + 1):
        if color[start] != 0:
            continue
        # BFS to find shortest cycle and assign colors
        color[start] = 1
        parent[start] = 0
        queue = [start]
        head = 0
        cycle = None
        while head < len(queue) and cycle is None:
            u = queue[head]; head += 1
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu
                    parent[v] = u
                    queue.append(v)
                elif v != parent[u]:
                    # found cycle
                    cycle = (u, v)
                    break
            if cycle is not None:
                break
        
        if cycle is not None:
            u, v = cycle
            # find path from u to v in BFS tree
            path_u = []
            x = u
            while x != 0:
                path_u.append(x)
                x = parent[x]
            path_v = []
            x = v
            while x != 0:
                path_v.append(x)
                x = parent[x]
            # find LCA
            set_u = set(path_u)
            lca = 0
            for node in path_v:
                if node in set_u:
                    lca = node
                    break
            # build cycle
            cyc = []
            x = u
            while x != lca:
                cyc.append(x)
                x = parent[x]
            cyc.append(lca)
            temp = []
            x = v
            while x != lca:
                temp.append(x)
                x = parent[x]
            cyc.extend(reversed(temp))
            L = len(cyc)
            if L % 2 == 1:
                print("NO")
                return
            # even cycle, need to flip colors along one path
            # path from u to lca (excluding lca) and from v to lca (excluding lca)
            # flip colors on path_u from u to lca (excluding lca)
            x = u
            while x != lca:
                color[x] = 3 - color[x]
                x = parent[x]
            # flip colors on path_v from v to lca (excluding lca)
            x = v
            while x != lca:
                color[x] = 3 - color[x]
                x = parent[x]
        
        # continue BFS to finish coloring this component
        while head < len(queue):
            u = queue[head]; head += 1
            cu = color[u]
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu
                    parent[v] = u
                    queue.append(v)
                elif v != parent[u]:
                    # another cycle, check consistency
                    if color[v] == color[u]:
                        print("NO")
                        return
    
    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()