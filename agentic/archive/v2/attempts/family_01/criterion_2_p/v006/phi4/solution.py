from sys import stdin, stdout

def solve():
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Try to assign items starting with line 1
    assignment = [None] * (n + 1)
    possible = True

    def dfs(node, color):
        nonlocal possible
        if assignment[node] is not None:
            if assignment[node] != color:
                possible = False
            return
        assignment[node] = color
        
        for neighbor in adj_list[node]:
            dfs(neighbor, 3 - color)

    # Try to assign each component starting with the smallest index
    for i in range(1, n + 1):
        if assignment[i] is None:
            dfs(i, 1)
    
    if not possible:
        print("NO")
    else:
        result = [min(assignment[i], assignment[i] ^ 3) for i in range(1, n + 1)]
        print("YES")
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()