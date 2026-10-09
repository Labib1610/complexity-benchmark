import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, k = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(set)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    if m == 0:
        # No edges, all nodes can be in the same group
        print("YES")
        print(' '.join(map(str, range(1, min(k, n) + 1))))
        return
    
    # Check if the graph is bipartite and find the two camps
    color = {}
    camps = [set(), set()]
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        camps[0].add(start)
        while queue:
            u = queue.popleft()
            c = color[u]
            for v in adj[u]:
                if v not in color:
                    color[v] = 1 - c
                    camps[1 - c].add(v)
                    queue.append(v)
                elif color[v] == c:
                    # Not bipartite, but problem guarantees it is
                    return False
        return True
    
    # Find all components
    visited = set()
    for i in range(1, n+1):
        if i not in color:
            if not bfs(i):
                # This shouldn't happen according to problem statement
                pass
    
    camp0 = list(camps[0])
    camp1 = list(camps[1])
    size0 = len(camp0)
    size1 = len(camp1)
    
    # For a group of k strangers, we can take at most one node from each pair that are connected
    # But since the graph is bipartite, we can take all nodes from one side as long as k <= size of that side
    # Actually, in a bipartite graph, the maximum independent set is the larger of the two sides
    # So we just need to check if k <= max(size0, size1)
    # And if so, take k nodes from the larger side
    
    if k <= size0:
        print("YES")
        print(' '.join(map(str, camp0[:k])))
    elif k <= size1:
        print("YES")
        print(' '.join(map(str, camp1[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    main()