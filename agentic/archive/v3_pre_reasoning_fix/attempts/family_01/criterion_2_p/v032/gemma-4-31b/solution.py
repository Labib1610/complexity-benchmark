import sys

# Increase recursion depth for deep DFS in large graphs
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
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # states: 0 = unvisited, 1 = state 1, 2 = state 2
    states = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence (s1, s2, ..., sn),
    # for each connected component, we want the smallest possible value
    # for the smallest index in that component.
    # Since the graph is bipartite, once the state of one node is fixed, 
    # all other nodes in the component are fixed.
    # For each component, we check if it's bipartite.
    # If it is, we have two choices for the coloring: (C1=1, C2=2) or (C1=2, C2=1).
    # To minimize the sequence lexicographically, we look at the smallest index 'i' 
    # in the component. We should try to set state[i] = 1.
    
    for i in range(1, n + 1):
        if states[i] == 0:
            component = []
            stack = [i]
            states[i] = 1 # Tentatively assign state 1 to the smallest index
            
            # BFS/DFS to find all nodes in component and check bipartiteness
            # Using a manual stack to avoid recursion limits and for efficiency
            visited_idx = 0
            component.append(i)
            
            # We use a queue-like approach with a list for BFS
            queue = [i]
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for v in adj[u]:
                    if states[v] == 0:
                        states[v] = 3 - states[u]
                        queue.append(v)
                    elif states[v] == states[u]:
                        print("NO")
                        return
            
            # The BFS already assigned states starting with states[i] = 1.
            # Because we process i from 1 to n, and for the first node in each 
            # component we try to set it to 1, this naturally leads to the 
            # lexicographically smallest assignment.
            # If states[i] = 1 is possible, it is always better than states[i] = 2.
    
    print("YES")
    print(*(states[1:]))

if __name__ == "__main__":
    solve()