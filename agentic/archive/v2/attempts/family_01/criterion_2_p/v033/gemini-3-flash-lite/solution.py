import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(300000)

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
        
    group = [0] * (n + 1)
    
    def dfs(u, c):
        group[u] = c
        for v in adj[u]:
            if group[v] == 0:
                if not dfs(v, 3 - c):
                    return False
            elif group[v] == c:
                return False
        return True

    # To get the lexicographically smallest sequence, we iterate 1 to n.
    # If a researcher is not assigned, we try assigning them to group 1.
    # If it fails, we try group 2.
    for i in range(1, n + 1):
        if group[i] == 0:
            # We want s_i = 1 if possible.
            # Temporarily save state to backtrack if needed
            temp_group = list(group)
            if not dfs(i, 1):
                # Backtrack and try group 2
                group = temp_group
                if not dfs(i, 2):
                    print("NO")
                    return
    
    print("YES")
    print(*(group[1:]))

solve()