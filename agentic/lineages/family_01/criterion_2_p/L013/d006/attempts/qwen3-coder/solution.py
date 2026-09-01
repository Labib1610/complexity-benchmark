import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = [[] for _ in range(n+1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # We need to check which pairs of transformations lead to a fixed point when composed.
    # Let's analyze f_u(f_v(V)) = V
    # There are 4 combinations:
    # (1,1): f1(f1(V)) = M*(M*V + B1) + B1 = M*M*V + M*B1 + B1 = V + M*B1 + B1
    # M*B1 = (0*1 + 1*(-1), 1*1 + 0*(-1)) = (-1, 1) = B2
    # So f1(f1(V)) = V + B2 + B1 = V + (0,0) => Fixed point exists => UNSTABLE
    #
    # (1,2): f1(f2(V)) = M*(M*V + B2) + B1 = V + M*B2 + B1 = V + B1 + B1 = V + 2*B1
    # No fixed point => STABLE
    #
    # (2,1): f2(f1(V)) = M*(M*V + B1) + B2 = V + M*B1 + B2 = V + B2 + B2 = V + 2*B2
    # No fixed point => STABLE
    #
    # (2,2): f2(f2(V)) = M*(M*V + B2) + B2 = V + M*B2 + B2 = V + B1 + B2 = V + (0,0)
    # Fixed point exists => UNSTABLE
    #
    # So the forbidden pairs are (1,1) and (2,2). 
    # This means adjacent nodes must have different transformations.
    # This is a 2-coloring problem.
    
    # Build adjacency list
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # 2-coloring with BFS/DFS. Color 1 and 2.
    color = [0] * (n+1)  # 0: unvisited, 1: color 1, 2: color 2
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        while queue:
            u = queue.popleft()
            c = color[u]
            for v in graph[u]:
                if color[v] == 0:
                    color[v] = 3 - c  # flip color
                    queue.append(v)
                elif color[v] == c:
                    return False  # conflict
        return True
    
    for i in range(1, n+1):
        if color[i] == 0:
            if not bfs(i):
                print("NO")
                return
    
    # If we reach here, a valid coloring exists.
    # To get lexicographically smallest, we prefer color 1 over 2.
    # Our BFS already ensures this since we start with color 1.
    print("YES")
    result = []
    for i in range(1, n+1):
        if color[i] == 0:
            result.append('1')
        else:
            result.append(str(color[i]))
    print(" ".join(result))

if __name__ == "__main__":
    main()