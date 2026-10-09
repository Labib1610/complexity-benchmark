import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if n == 0:
        print("YES")
        return
    
    adj = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)  # 0: unvisited, 1: color 1, 2: color 2
    
    # Check if bipartite using BFS and find lexicographically smallest coloring
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 3 - current_color  # flips 1->2 and 2->1
            
            for neighbor in adj[node]:
                if color[neighbor] == 0:
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    return False  # Not bipartite
        return True
    
    # Process nodes in order 1 to n to ensure lexicographically smallest solution
    for i in range(1, n + 1):
        if color[i] == 0:
            if not bfs(i):
                print("NO")
                return
    
    # If we reach here, a valid coloring exists
    print("YES")
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append('1')  # Isolated node can be assigned 1
        else:
            result.append(str(color[i]))
    print(' '.join(result))

if __name__ == "__main__":
    main()