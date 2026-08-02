import sys

# Increase recursion depth for deep components
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
            # Self-loop means it's impossible to assign different periods
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
    
    # color[i] will be 0 (unvisited), 1, or 2
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest assignment, 
    # we process nodes in increasing order of their indices.
    # For each connected component, we try assigning 1 to the smallest node in that component.
    # Since we want lexicographically smallest, the first node we encounter in a component 
    # should be assigned 1 if possible. 
    # Actually, in a bipartite graph, once the color of one node is fixed, 
    # the colors of all reachable nodes are fixed.
    # To minimize the sequence (s1, s2, ..., sn), for each component, we compare 
    # the resulting sequence if the root is 1 vs if the root is 2.
    # However, the root is always the smallest index in the component.
    # If we set root = 1, we get a sequence. If we set root = 2, 
    # every node in that component flips (1->2, 2->1).
    # Since the root is the smallest index, setting root = 1 always results in 
    # a lexicographically smaller sequence for that component.
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS to color the component
            # Root of the component is i. Assign color[i] = 1.
            stack = [i]
            color[i] = 1
            component = [i]
            
            # Use iterative DFS to avoid recursion depth issues and collect component
            visited_ptr = 0
            queue = [i]
            while visited_ptr < len(queue):
                u = queue[visited_ptr]
                visited_ptr += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # The logic above: for each component, the smallest index i is assigned 1.
    # This ensures s_i is as small as possible. Since i is the first index 
    # in the sequence for this component, this is the greedy choice for 
    # lexicographical minimality.
    
    print("YES")
    print(*(color[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()