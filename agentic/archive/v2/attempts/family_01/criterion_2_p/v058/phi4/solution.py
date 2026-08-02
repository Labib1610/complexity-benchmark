from sys import stdin, stdout

def main():
    n, m = map(int, stdin.readline().split())
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        
    settings = [0] * n
    valid = True

    def dfs(node, current_setting):
        nonlocal valid
        if settings[node]:
            return settings[node] == current_setting
        settings[node] = current_setting
        for neighbor in adj[node]:
            if not dfs(neighbor, 3 - current_setting):  # Flip between 1 and 2
                valid = False
                return False
        return True

    for i in range(n):
        if not settings[i]:
            if not dfs(i, 1):
                valid = False
                break
    
    if valid:
        stdout.write("YES\n")
        stdout.write(" ".join(map(str, settings)) + "\n")
    else:
        stdout.write("NO\n")

if __name__ == "__main__":
    main()