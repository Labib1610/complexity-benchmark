import sys
from collections import defaultdict, deque

def solve():
    import sys
    import threading

    def main():
        import sys
        sys.setrecursionlimit(1 << 25)
        
        n, m, k = map(int, sys.stdin.readline().split())
        
        if m == 0:
            print("YES")
            print(' '.join(map(str, range(1, k+1))))
            return
        
        # Build adjacency list
        adj = defaultdict(list)
        edges = []
        for _ in range(m):
            u, v = map(int, sys.stdin.readline().split())
            adj[u].append(v)
            adj[v].append(u)
            edges.append((u, v))
        
        # Since the graph satisfies the polarity condition,
        # it's bipartite. We can color it with 2 colors.
        color = [0] * (n + 1)  # 0: unvisited, 1: color A, -1: color B
        visited = [False] * (n + 1)
        
        def bfs(start):
            queue = deque()
            queue.append(start)
            color[start] = 1
            visited[start] = True
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        color[v] = -color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        # This should not happen due to problem guarantee
                        pass
        
        # Color all components
        for i in range(1, n + 1):
            if not visited[i]:
                bfs(i)
        
        # Separate nodes into two groups based on color
        group1 = []
        group2 = []
        for i in range(1, n + 1):
            if color[i] == 1:
                group1.append(i)
            else:
                group2.append(i)
        
        # Try to take k nodes from either group1 or group2
        if len(group1) >= k:
            print("YES")
            print(' '.join(map(str, group1[:k])))
        elif len(group2) >= k:
            print("YES")
            print(' '.join(map(str, group2[:k])))
        else:
            # Try combining from both groups, but since they are independent,
            # we can just take up to len(group1) + len(group2)
            total = len(group1) + len(group2)
            if total >= k:
                # Take as many as needed from both
                res = group1[:]
                needed = k - len(res)
                res.extend(group2[:needed])
                print("YES")
                print(' '.join(map(str, res)))
            else:
                print("NO")

    threading.Thread(target=main).start()

solve()