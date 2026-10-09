import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        w = int(next(it)) - 1
        edges.append((u, w))
        adj[u].append(w)
        adj[w].append(u)

    # Precompute allowed pairs
    # ok[u][w][x][y] = True if assigning x to u and y to w is fine
    ok = [[[[False]*3 for _ in range(3)] for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for w in range(n):
            for x in range(1,4):
                for y in range(1,4):
                    diff = (x**3)*(w+1-1) + x*y*(u*x - w*y) + (y**3)*(1-u-1)  # wait, careful
                    # Actually use formula:
                    diff = (x**3)*(w-1) + x*y*(u*x - w*y) + (y**3)*(1-u)
                    ok[u][w][x-1][y-1] = (diff != 0)

    # Backtracking
    assign = [0]*n
    used = [False]*n

    def backtrack(idx):
        if idx == n:
            return True
        # Try speeds 1,2,3
        for sp in [1,2,3]:
            assign[idx] = sp
            good = True
            for nb in adj[idx]:
                if assign[nb] != 0:
                    if not ok[idx][nb][sp-1][assign[nb]-1]:
                        good = False
                        break
            if good:
                if backtrack(idx+1):
                    return True
        assign[idx] = 0
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(str(x) for x in assign))
    else:
        print("NO")

if __name__ == "__main__":
    solve()