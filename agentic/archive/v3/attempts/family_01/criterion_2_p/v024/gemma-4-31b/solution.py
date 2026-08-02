import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(300000)

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        if u == v:
            # Self-loop makes it impossible to 2-color
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    # color[i] will be 0 (unvisited), 1, or 2
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, 
    # for each connected component, we want the smallest possible 
    # value for the smallest index in that component.
    # Since we only have colors 1 and 2, we should try to set 
    # the smallest index in the component to 1.
    # If the component is bipartite, there are exactly two ways to color it.
    # One way starts with the smallest index as 1, the other as 2.
    # 1 is always smaller than 2, so we always prefer the assignment 
    # where the smallest index in the component is 1.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS to color the component
            # We force the first node encountered (which is the smallest index in this component) to be 1
            stack = [i]
            color[i] = 1
            
            # Use a simple stack for DFS to avoid recursion limits and be efficient
            visited_count = 0
            component_nodes = []
            
            # Standard bipartite check using BFS/DFS
            # We use a list as a queue for BFS to ensure we process in a stable manner
            queue = [i]
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    print("YES")
    print(*(color[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()