import sys

# Increase recursion depth for deep components in the graph
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
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # color[i] = 0 means unvisited, 1 or 2 means shift assignment
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, for each connected component,
    # we must decide whether the smallest index in that component gets shift 1 or 2.
    # However, since we want the smallest sequence overall, for each component,
    # we should try to assign the smallest index in that component to shift 1.
    # If we do that, the colors of all other nodes in that component are fixed.
    # Then we check if this assignment is valid (bipartite).
    # If it is, we check if swapping 1s and 2s in that component would result in a 
    # lexicographically smaller sequence. 
    # Actually, the simplest way to get the lexicographically smallest is:
    # For each unvisited node i (from 1 to n), it must be the smallest index in its component.
    # To make the sequence lexicographically smallest, we MUST try to set s_i = 1.
    # This will then force the colors of all other nodes in the component.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS to color the component. 
            # Smallest index in component gets 1 to be lexicographically smallest.
            stack = [(i, 1)]
            color[i] = 1
            component = []
            
            # Use iterative DFS to avoid recursion limits and for speed
            q = [i]
            visited_in_comp = {i}
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                component.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
    print("YES")
    print(*(color[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()