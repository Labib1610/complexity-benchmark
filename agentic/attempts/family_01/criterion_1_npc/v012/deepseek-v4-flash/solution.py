import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    colors = [0] * n  # 0 = unassigned, 1,2,3 = colors

    # Check if we can color the graph with 3 colors using backtracking
    # We try colors in order 1,2,3 to get lexicographically smallest
    def backtrack(idx):
        if idx == n:
            return True
        for c in (1, 2, 3):
            # check if any neighbor has same color
            ok = True
            for nb in adj[idx]:
                if colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[idx] = c
                if backtrack(idx + 1):
                    return True
                colors[idx] = 0
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()