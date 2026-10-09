import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # mode[u] = 0: unassigned, 1: transmitter, 2: receiver
    mode = [0] * n
    
    for start in range(n):
        if mode[start] != 0:
            continue
        
        # BFS for this connected component
        queue = deque()
        queue.append(start)
        mode[start] = 1  # Assign lexicographically smallest mode (1)
        
        # Track nodes in this component for potential rollback
        component_nodes = []
        component_nodes.append(start)
        
        possible = True
        
        while queue:
            u = queue.popleft()
            
            for v in adj[u]:
                if mode[v] == 0:
                    mode[v] = 3 - mode[u]  # Assign opposite mode
                    queue.append(v)
                    component_nodes.append(v)
                elif mode[v] == mode[u]:
                    possible = False
                    break
            if not possible:
                break
        
        if not possible:
            # Try assigning start as mode 2
            # Reset modes for this component
            for node in component_nodes:
                mode[node] = 0
            
            queue.append(start)
            mode[start] = 2
            possible2 = True
            
            while queue:
                u = queue.popleft()
                
                for v in adj[u]:
                    if mode[v] == 0:
                        mode[v] = 3 - mode[u]
                        queue.append(v)
                    elif mode[v] == mode[u]:
                        possible2 = False
                        break
                if not possible2:
                    break
            
            if not possible2:
                print("NO")
                return
    
    print("YES")
    print(' '.join(map(str, mode)))

if __name__ == "__main__":
    solve()