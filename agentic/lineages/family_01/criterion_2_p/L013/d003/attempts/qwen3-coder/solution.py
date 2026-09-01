import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    graph = defaultdict(list)
    
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # The condition for a tether to be balanced:
    # For nodes with values a and b (each is 1 or 2):
    # a*b + a + b = 5
    # This can be rewritten as: (a+1)(b+1) = 6
    # Since a,b are in {1,2}, we have (a+1) in {2,3} and (b+1) in {2,3}
    # The only way to get 6 is 2*3 or 3*2
    # So one of a,b must be 1 and the other must be 2.
    # That is, for every edge, the two endpoints must have different values.
    
    # This is a 2-coloring (bipartite) problem.
    
    color = [-1] * n  # -1: unvisited, 0: color 1, 1: color 2
    
    # Check each connected component
    for start in range(n):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0  # Assign color 0 (value 1)
            
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # If we reach here, a valid assignment exists.
    # We want the lexicographically smallest one.
    # That means we want the earliest nodes to be as small as possible.
    # Color 0 corresponds to value 1, color 1 corresponds to value 2.
    # To get the lex smallest, we should use 0 (value 1) for node 0 if possible.
    # But we already fixed color[0] = 0 if node 0 was the start of a component.
    # Actually, in our BFS, we start from node 0 first, so color[0] is already set to 0.
    # So the coloring we have is already the lex smallest.
    
    result = []
    for i in range(n):
        if color[i] == 0:
            result.append('1')
        else:
            result.append('2')
    
    print("YES")
    print(' '.join(result))

if __name__ == "__main__":
    main()