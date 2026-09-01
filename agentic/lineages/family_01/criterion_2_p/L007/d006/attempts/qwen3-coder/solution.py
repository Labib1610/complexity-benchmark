import sys
from collections import defaultdict

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
    adj = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        index += 2

    # Precompute the squared magnitude of cross products
    # v1 = (1,2,3), v2 = (3,1,2)
    # v1 x v1 = (0,0,0) => squared magnitude = 0
    # v2 x v2 = (0,0,0) => squared magnitude = 0
    # v1 x v2 = (2*2 - 3*1, 3*3 - 1*2, 1*1 - 2*3) = (4-3, 9-2, 1-6) = (1, 7, -5) => squared magnitude = 1+49+25 = 75
    # So:
    # same grades (1,1) or (2,2): contribution = 0
    # different grades (1,2) or (2,1): contribution = 75
    
    # For the total to be 75 * m, all edges must contribute 75 => all edges must connect different grades
    # This is a 2-coloring (bipartite) problem.
    
    color = [-1] * (n + 1)
    
    # Check if the graph is bipartite
    def bfs(start):
        from collections import deque
        queue = deque()
        queue.append(start)
        color[start] = 0
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    # Check all components
    for i in range(1, n + 1):
        if color[i] == -1:
            if not bfs(i):
                print("NO")
                return
    
    # If bipartite, assign grades: color 0 -> grade 1, color 1 -> grade 2
    # For lexicographically smallest, we want node 1 to have grade 1 if possible.
    # If color[1] == 1, we can flip all colors (0->1, 1->0) to make color[1] = 0
    if color[1] == 1:
        for i in range(1, n + 1):
            color[i] ^= 1
    
    # Now color[i] = 0 means grade 1, color[i] = 1 means grade 2
    grades = []
    for i in range(1, n + 1):
        grades.append(str(color[i] + 1))  # 0->1, 1->2
    
    print("YES")
    print(" ".join(grades))

if __name__ == "__main__":
    main()