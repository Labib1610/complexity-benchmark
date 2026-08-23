import sys

# Increase recursion depth for deep components in DFS
sys.setrecursionlimit(300000)

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        ptr += 2
        if u == v:
            # A person cannot be mutually exclusive with themselves
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
    
    # s[i] will store the work period (1 or 2). 0 means unassigned.
    s = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, we process nodes 1 to n.
    # For each connected component, the first node we encounter (the smallest index)
    # should be assigned to 1 if possible.
    for i in range(1, n + 1):
        if s[i] == 0:
            # Start a BFS or iterative DFS to avoid recursion depth issues
            # and to ensure we process the component.
            # The first node in the component (i) is assigned 1 to minimize lexicographically.
            s[i] = 1
            stack = [i]
            while stack:
                u = stack.pop()
                current_val = s[u]
                next_val = 2 if current_val == 1 else 1
                
                for v in adj[u]:
                    if s[v] == 0:
                        s[v] = next_val
                        stack.append(v)
                    elif s[v] == current_val:
                        # Not bipartite
                        print("NO")
                        return
    
    # If we reached here, a valid 2-coloring exists.
    # Since we processed nodes 1..n and assigned the first node of each component 1,
    # and since the constraints are only "must be different", 
    # the assignment is uniquely determined within each component once the first node is fixed.
    # To minimize lexicographically, for each component, we check if swapping 1s and 2s
    # results in a smaller sequence.
    # Actually, for a connected component, if we fix the first node (smallest index) as 1,
    # any other assignment (fixing it as 2) would result in a larger sequence 
    # because the first element of the sequence that differs would be 1 vs 2.
    
    print("YES")
    print(*(s[1:]))

if __name__ == "__main__":
    solve()