import sys

# Increase recursion depth for deep DFS in bipartite components
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
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # team[i] = 0 means unassigned, 1 or 2 means assigned team
    team = [0] * (n + 1)
    
    # To get the lexicographically smallest assignment, 
    # we process nodes in order from 1 to n.
    # For each connected component, we have two choices for the first node.
    # If the first node of a component is assigned team 1, it might lead to a 
    # lexicographically smaller sequence than assigning it team 2.
    # However, the choice for the first node in a component affects all others.
    # Let the first node in the component be 'root'. 
    # Let the two possible colorings be C1 and C2, where C1(root)=1 and C2(root)=2.
    # C2 is simply the inversion of C1 (1 <-> 2).
    # To make the sequence lexicographically smallest, we compare C1 and C2.
    # The first index i in the component where C1[i] != C2[i] determines the winner.
    # Since C1[root]=1 and C2[root]=2, and root is the smallest index in the component,
    # C1 will always be lexicographically smaller than C2.
    # Thus, for every component, we MUST assign the smallest index in that component to team 1.
    
    for i in range(1, n + 1):
        if team[i] == 0:
            # Start BFS/DFS to color the component
            # Smallest index in component gets team 1
            stack = [(i, 1)]
            team[i] = 1
            component = []
            
            # Using a stack for iterative DFS to avoid recursion limit and for speed
            q = [i]
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                for v in adj[u]:
                    if team[v] == 0:
                        team[v] = 3 - team[u]
                        q.append(v)
                    elif team[v] == team[u]:
                        print("NO")
                        return
    
    print("YES")
    print(*(team[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()