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
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        ptr += 2
        if u == v:
            # Self-loop makes it impossible to 2-color
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    # s[i] will store the segment (1 or 2). 0 means unvisited.
    s = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, we process components
    # in order from 1 to n. For the first node i of a component, 
    # we try setting s[i] = 1 first.
    # However, a simple BFS/DFS doesn't guarantee lexicographical smallest 
    # if we just set the first node to 1. 
    # Actually, for each connected component, there are only two possible 
    # 2-colorings (if it is bipartite).
    # One coloring starts with node 'root' as 1, the other as 2.
    # To minimize the sequence s_1, s_2, ..., s_n, for each component, 
    # we compare the two possible assignments and pick the lexicographically smaller one.
    
    for i in range(1, n + 1):
        if s[i] == 0:
            # New component found. Find all nodes in this component.
            component = []
            stack = [i]
            s[i] = 1 # Temporarily assign 1 to root
            
            # Use a temporary list to track the coloring of this component
            # to determine which of the two valid 2-colorings is lexicographically smaller.
            visited_in_comp = {i}
            q = [i]
            idx = 0
            while idx < len(q):
                u = q[idx]
                idx += 1
                for v in adj[u]:
                    if s[v] == 0:
                        s[v] = 3 - s[u]
                        q.append(v)
                        visited_in_comp.add(v)
                    elif s[v] == s[u]:
                        print("NO")
                        return
            
            # Now we have one valid coloring for this component.
            # The only other valid coloring is flipping 1 <-> 2.
            # To make the sequence lexicographically smallest, we look at 
            # the smallest index in the component. 
            # The smallest index is 'i'. To make the sequence smallest,
            # we want s[i] to be as small as possible.
            # Since we already set s[i] = 1, and 1 is the smallest possible value,
            # this is already the lexicographically smallest choice for this component.
            # If we had set s[i] = 2, we would have had to flip everything.
            # Since the first element of the component we encounter is i, 
            # setting s[i] = 1 is always optimal for the lexicographical order.
            pass

    print("YES")
    print(*(s[1:]))

if __name__ == "__main__":
    solve()