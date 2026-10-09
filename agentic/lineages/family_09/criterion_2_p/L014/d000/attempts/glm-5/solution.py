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
    
    color = [0] * (n + 1)
    counts = [0, 0]
    
    # BFS to 2-color the graph
    # The graph is bipartite due to the problem's guarantee
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = [start]
            color[start] = 1
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                counts[color[u] - 1] += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
    
    # Choose the color with more nodes (or color 1 if tied)
    target_color = 1
    if counts[1] > counts[0]:
        target_color = 2
    
    # Check if we have enough nodes of the target color
    if counts[target_color - 1] >= k:
        res = [str(i) for i in range(1, n + 1) if color[i] == target_color]
        print("YES")
        print(" ".join(res[:k]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()