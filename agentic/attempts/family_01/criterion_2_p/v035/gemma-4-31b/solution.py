import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(300000)

def solve():
    # Use fast I/O
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
            # Self-loop means employee cannot be in either shift
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    # color[i] will store the shift (1 or 2). 0 means unvisited.
    color = [0] * (n + 1)
    
    # To find the lexicographically smallest assignment, we want s_i to be 1 
    # as much as possible for i = 1, 2, ..., n.
    # For each connected component, the first node encountered in order 1..n
    # should be assigned 1. Then all other nodes in that component are 
    # determined relative to that choice.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start a BFS to color the component. 
            # Since we process nodes i from 1 to n, and we want the smallest 
            # lexicographical sequence, we must set color[i] = 1.
            stack = [i]
            color[i] = 1
            
            # Using a stack for DFS or queue for BFS. 
            # To avoid recursion depth issues and ensure correctness:
            ptr = 0
            queue = [i]
            while ptr < len(queue):
                u = queue[ptr]
                ptr += 1
                
                for v in adj[u]:
                    if color[v] == 0:
                        # Assign opposite color
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        # Not bipartite
                        print("NO")
                        return

    # If we reached here, it's bipartite.
    print("YES")
    print(*(color[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()