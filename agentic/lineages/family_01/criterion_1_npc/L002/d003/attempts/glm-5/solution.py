import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # For each node, track which values are forbidden by assigned neighbors
    forbidden = [set() for _ in range(n)]
    assignment = [0] * n
    
    def dfs(u):
        # Find the smallest valid value for u
        for val in [1, 2, 3]:
            if val not in forbidden[u]:
                assignment[u] = val
                # Propagate constraint: neighbors cannot have same value
                newly_forbidden = []
                for v in adj[u]:
                    if val not in forbidden[v]:
                        forbidden[v].add(val)
                        newly_forbidden.append(v)
                
                # Find next unassigned node
                next_node = -1
                for i in range(n):
                    if assignment[i] == 0:
                        next_node = i
                        break
                
                if next_node == -1:
                    return True
                
                if dfs(next_node):
                    return True
                
                # Backtrack: remove constraints
                for v in newly_forbidden:
                    forbidden[v].remove(val)
                assignment[u] = 0
        
        return False
    
    if dfs(0):
        print("YES")
        print(" ".join(map(str, assignment)))
    else:
        print("NO")

solve()