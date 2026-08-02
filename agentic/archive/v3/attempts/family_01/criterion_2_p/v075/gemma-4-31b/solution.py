import sys

# Increase recursion depth for deep components
sys.setrecursionlimit(300000)

def solve():
    # Read n and m
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
            # A technician cannot be in a conflict with themselves
            # as they cannot be in different shifts.
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    # shift[i] will store the assignment (1 or 2), 0 means unassigned
    shift = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, we process nodes from 1 to n.
    # For each connected component, the first node we encounter (the smallest index)
    # should be assigned shift 1 if possible.
    # However, assigning the first node of a component to 1 doesn't guarantee 
    # lexicographical smallest for the whole sequence because nodes within 
    # the component are constrained by bipartiteness.
    # Actually, for a bipartite component, there are only two possible colorings.
    # One where the first node is 1, and one where it is 2.
    # To minimize the sequence (s1, s2, ..., sn), we must decide for each component
    # which of the two colorings to pick.
    # Let the first node encountered in the component be 'root'.
    # Let the two possible colorings be C1 (root=1) and C2 (root=2).
    # We compare C1 and C2 lexicographically.
    # C1 is better if the first index i where C1[i] != C2[i] has C1[i] < C2[i].
    # Since C1 and C2 are exact opposites (C1[i]=1 <=> C2[i]=2), the first index i
    # where they differ is the root itself. Since C1[root]=1 and C2[root]=2, 
    # C1 is always lexicographically smaller.
    
    for i in range(1, n + 1):
        if shift[i] == 0:
            # Start BFS/DFS to color the component
            # Root of component is i, assign it shift 1
            stack = [(i, 1)]
            shift[i] = 1
            component = []
            
            # Using a manual stack to avoid recursion depth issues
            visited_in_comp = []
            q = [i]
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                visited_in_comp.append(u)
                for v in adj[u]:
                    if shift[v] == 0:
                        shift[v] = 3 - shift[u]
                        q.append(v)
                    elif shift[v] == shift[u]:
                        print("NO")
                        return
            
    print("YES")
    print(*(shift[1:]))

if __name__ == "__main__":
    solve()