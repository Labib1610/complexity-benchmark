import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * (n + 1)
    is_bipartite = True
    
    # BFS/DFS to check bipartiteness and color
    # Since the graph satisfies the even-sequence property, it must be bipartite.
    # We just need to color it.
    
    for start in range(1, n + 1):
        if color[start] == -1:
            # BFS
            queue = [start]
            color[start] = 0
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        # This case shouldn't happen given the problem guarantee
                        is_bipartite = False
    
    # Count nodes in each color
    count0 = color.count(0)
    count1 = n - count0
    
    if count0 >= k:
        print("YES")
        res = [str(i) for i in range(1, n + 1) if color[i] == 0]
        print(" ".join(res[:k]))
    elif count1 >= k:
        print("YES")
        res = [str(i) for i in range(1, n + 1) if color[i] == 1]
        print(" ".join(res[:k]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()