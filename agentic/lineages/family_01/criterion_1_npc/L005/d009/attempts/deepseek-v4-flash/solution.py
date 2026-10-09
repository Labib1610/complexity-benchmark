import sys

def solve():
    input_data = sys.stdin.read().strip().split()
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

    color = [-1] * n

    def backtrack(node):
        if node == n:
            return True
        # Try colors 0,1,2 (representing missing metric)
        for c in range(3):
            ok = True
            for nb in adj[node]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1
        return False

    if backtrack(0):
        # Map color to package:
        # color 0 -> missing Turbidity -> package 1
        # color 1 -> missing Pressure -> package 2
        # color 2 -> missing Salinity -> package 3
        pkg = [0] * n
        for i in range(n):
            if color[i] == 0:
                pkg[i] = 1
            elif color[i] == 1:
                pkg[i] = 2
            else:
                pkg[i] = 3
        print("YES")
        print(" ".join(map(str, pkg)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()