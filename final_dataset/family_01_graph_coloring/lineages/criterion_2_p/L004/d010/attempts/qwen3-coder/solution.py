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
    graph = defaultdict(list)
    degree = [0] * (n + 1)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Check if any vertex has degree > 2
    # Because each edge contributes to a penalty of either 20 or -10
    # We want total penalty = -4 * m
    # Let x = number of edges with penalty 20, y = number with penalty -10
    # Then 20x - 10y = -4m and x + y = m => 20x - 10(m - x) = -4m => 20x - 10m + 10x = -4m => 30x = 6m => x = m/5
    # So m must be divisible by 5 and x = m/5, y = 4m/5
    
    # But let's think differently. For each edge (u,v):
    # If s_u=1, s_v=1: C_u=(1,2,3,4), C_v=(1,2,3,4) => dot = 1*1+2*2+3*3+4*4 = 30
    # If s_u=1, s_v=2: C_u=(1,2,3,4), C_v=(4,-3,-2,1) => dot = 1*4+2*(-3)+3*(-2)+4*1 = 4-6-6+4 = -4
    # If s_u=2, s_v=1: C_u=(4,-3,-2,1), C_v=(1,2,3,4) => dot = 4*1+(-3)*2+(-2)*3+1*4 = 4-6-6+4 = -4
    # If s_u=2, s_v=2: C_u=(4,-3,-2,1), C_v=(4,-3,-2,1) => dot = 16+9+4+1 = 30
    
    # So we can have penalties of 30 or -4.
    # Want sum = -4m.
    # Let x = number of edges with penalty 30, y = number with penalty -4.
    # 30x - 4y = -4m and x + y = m => 30x - 4(m - x) = -4m => 30x - 4m + 4x = -4m => 34x = 0 => x = 0
    # So all edges must have penalty -4. That means for every edge (u,v), s_u != s_v.
    # This is a bipartite graph coloring problem.
    
    # Color the graph with 2 colors such that adjacent nodes have different colors.
    # Also, we want the lexicographically smallest assignment.
    # Assign color 1 to the first node, then do BFS.
    
    color = [-1] * (n + 1)  # -1: unvisited, 0: color 1, 1: color 2
    
    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0  # Assign color 1 (0 represents 1)
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 1 - current_color
                
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] == current_color:
                        print("NO")
                        return
    
    # If we reach here, a valid 2-coloring exists.
    # Convert color 0 -> 1, color 1 -> 2
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append('1')
        else:
            result.append('2')
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()