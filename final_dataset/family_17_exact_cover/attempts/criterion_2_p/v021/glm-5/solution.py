import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    
    adj = [[] for _ in range(q + 1)]
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        adj[a].append(b)
        idx += 2
        
    match_R = [0] * (2 * q + 1)
    visited = [0] * (q + 1)
    iteration = 0
    
    def dfs(u):
        stack = [(u, 0)]
        while stack:
            curr, i = stack[-1]
            if i == 0:
                visited[curr] = iteration
            if i < len(adj[curr]):
                v = adj[curr][i]
                stack[-1] = (curr, i + 1)
                if match_R[v] == 0 or (visited[match_R[v]] != iteration and dfs(match_R[v])):
                    match_R[v] = curr
                    return True
            else:
                stack.pop()
        return False

    for u in range(1, q + 1):
        iteration += 1
        if not dfs(u):
            print("NO")
            return
            
    print("YES")
    for v in range(q + 1, 2 * q + 1):
        if match_R[v] != 0:
            print(match_R[v], v)

if __name__ == '__main__':
    solve()