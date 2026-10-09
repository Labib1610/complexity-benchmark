import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build graph
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Color array: 0 = unvisited, 1 = color 1, 2 = color 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 3 - current_color  # flips 1->2 and 2->1
            for neighbor in graph[node]:
                if color[neighbor] == 0:
                    color[neighbor] = next_color
                    queue.append(neighbor)
                elif color[neighbor] != next_color:
                    return False
        return True
    
    # Process each connected component
    for i in range(1, n + 1):
        if color[i] == 0:
            if not bfs(i):
                print("NO")
                return
    
    # If we reach here, a valid assignment exists
    # Ensure lexicographically smallest by starting with person 1 in period 1 if possible
    # Actually, since we process nodes in order and always start with color 1,
    # and the graph is bipartite, this already ensures lex smallest.
    # But we need to make sure that for each component, the smaller color for the first node is chosen.
    # However, our BFS already starts with color 1 for the first node encountered.
    # So the result should be correct.
    
    print("YES")
    print(' '.join(str(c) for c in color[1:]))

if __name__ == "__main__":
    main()