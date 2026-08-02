import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(10**6)

def solve():
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
        
    state = [0] * (n + 1)
    
    # We want the lexicographically smallest assignment.
    # We iterate i from 1 to n. If unit i is unassigned, 
    # we try assigning it state 1. If it's forced by existing constraints,
    # it might be invalid.
    
    for i in range(1, n + 1):
        if state[i] == 0:
            # Try setting state[i] = 1
            # Use a stack for DFS to avoid recursion depth issues
            component = []
            stack = [(i, 1)]
            state[i] = 1
            component.append(i)
            
            possible = True
            ptr = 0
            while ptr < len(component):
                u = component[ptr]
                ptr += 1
                for v in adj[u]:
                    if state[v] == 0:
                        state[v] = 3 - state[u]
                        component.append(v)
                    elif state[v] == state[u]:
                        possible = False
                        break
                if not possible:
                    break
            
            if not possible:
                # If setting 1 failed, backtrack and try setting 2
                for node in component:
                    state[node] = 0
                
                stack = [(i, 2)]
                state[i] = 2
                component = [i]
                possible = True
                ptr = 0
                while ptr < len(component):
                    u = component[ptr]
                    ptr += 1
                    for v in adj[u]:
                        if state[v] == 0:
                            state[v] = 3 - state[u]
                            component.append(v)
                        elif state[v] == state[u]:
                            possible = False
                            break
                    if not possible:
                        break
                
                if not possible:
                    print("NO")
                    return

    print("YES")
    print(*(state[1:]))

solve()