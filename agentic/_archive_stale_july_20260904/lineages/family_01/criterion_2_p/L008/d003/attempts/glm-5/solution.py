import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input[ptr])
        ptr += 1
        v = int(input[ptr])
        ptr += 1
        adj[u].append(v)
        adj[v].append(u)
    
    # s[i] = 0: unassigned, 1: assigned 1, 2: assigned 2
    s = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if s[start] != 0:
            continue
        
        # BFS from start, trying to assign lexicographically smallest
        queue = deque()
        queue.append(start)
        s[start] = 1  # Try assigning 1 first (lexicographically smallest)
        
        # Track nodes in this component for potential rollback
        component_nodes = [start]
        conflict = False
        
        while queue and not conflict:
            u = queue.popleft()
            for v in adj[u]:
                if s[v] == 0:
                    # Assign the smallest valid value for v
                    # Check what values work with u
                    valid_for_v = []
                    for val in [1, 2]:
                        joint = 10 * s[u] + val
                        if joint % 3 == 0:
                            valid_for_v.append(val)
                    
                    if not valid_for_v:
                        conflict = True
                        break
                    elif len(valid_for_v) == 1:
                        s[v] = valid_for_v[0]
                    else:
                        # Both 1 and 2 work, pick smallest (1)
                        s[v] = 1
                    
                    queue.append(v)
                    component_nodes.append(v)
                else:
                    # Check if existing assignment is compatible
                    joint = 10 * s[u] + s[v]
                    if joint % 3 != 0:
                        conflict = True
                        break
        
        if conflict:
            # Try assigning start = 2
            for node in component_nodes:
                s[node] = 0
            
            queue = deque()
            queue.append(start)
            s[start] = 2
            component_nodes = [start]
            conflict = False
            
            while queue and not conflict:
                u = queue.popleft()
                for v in adj[u]:
                    if s[v] == 0:
                        valid_for_v = []
                        for val in [1, 2]:
                            joint = 10 * s[u] + val
                            if joint % 3 == 0:
                                valid_for_v.append(val)
                        
                        if not valid_for_v:
                            conflict = True
                            break
                        elif len(valid_for_v) == 1:
                            s[v] = valid_for_v[0]
                        else:
                            s[v] = 1
                        
                        queue.append(v)
                        component_nodes.append(v)
                    else:
                        joint = 10 * s[u] + s[v]
                        if joint % 3 != 0:
                            conflict = True
                            break
            
            if conflict:
                print("NO")
                return
    
    print("YES")
    print(' '.join(map(str, s[1:])))

solve()