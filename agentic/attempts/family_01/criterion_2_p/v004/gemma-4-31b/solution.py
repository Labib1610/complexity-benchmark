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
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        ptr += 2
        if u == v:
            # Self-loop means impossible to satisfy (u cannot be in same division as u)
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    # To get the lexicographically smallest sequence, we want to assign 
    # the smallest possible value (1) to the smallest indices first.
    # The personnel are partitioned into connected components.
    # For each component, once the first node's assignment is fixed, 
    # the rest are determined by the bipartite constraint.
    
    assignment = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # New connected component. 
            # To be lexicographically smallest, we want s_i to be 1 if possible.
            # Since it's the first node of the component, we can always try 1.
            stack = [(i, 1)]
            assignment[i] = 1
            component = [i]
            
            idx = 0
            while idx < len(stack):
                u, color = stack[idx]
                idx += 1
                
                next_color = 3 - color # 1 -> 2, 2 -> 1
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = next_color
                        stack.append((v, next_color))
                        component.append(v)
                    elif assignment[v] == color:
                        print("NO")
                        return
            
            # Now we have a valid 2-coloring for this component.
            # But we must check if swapping 1s and 2s in this component 
            # results in a lexicographically smaller sequence.
            # The sequence is s_1, s_2, ..., s_n.
            # For a component, the first node (smallest index) determines the 
            # lexicographical priority. Since we already set the smallest 
            # index in the component to 1, and 1 < 2, this is already the 
            # lexicographically smallest choice for this component.
            # (If we swapped, the first node would become 2, which is larger).

    print("YES")
    print(*(assignment[1:]))

if __name__ == "__main__":
    solve()