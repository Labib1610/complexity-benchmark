import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    receptor = [0] * (k + 1)
    adj = [[] for _ in range(k + 1)]
    for _ in range(t):
        x, y, z = map(int, input().split())
        receptor[x] = y
        adj[x].append(z)
    # bipartite matching: left = protein chains 1..k, right = enzymes 1..k
    match_right = [-1] * (k + 1)  # which protein chain is matched to enzyme z
    def dfs(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match_right[v] == -1 or dfs(match_right[v], visited):
                    match_right[v] = u
                    return True
        return False

    for u in range(1, k+1):
        visited = [False] * (k + 1)
        if not dfs(u, visited):
            # cannot match all
            print("NO")
            return

    # check if all matched
    if all(match_right[1:] != -1):
        print("YES")
        # build output
        for z in range(1, k+1):
            x = match_right[z]
            y = receptor[x]
            print(f"{x} {y} {z}")
    else:
        print("NO")

if __name__ == "__main__":
    solve()