import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -=  ​1
        v -=  ​1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n

    # Precompute degrees for tie-breaking
    deg = [len(adj[i]) for i in range(n)]

    def backtrack():
        # Find uncolored vertex with most colored neighbors
        best = -1
        best_score = -1
        best_deg = -1
        for i in range(n):
            if color[i] == 0:
                cnt =  ​0
                for nb in adj[i]:
                    if color[nb] != 0:
                        cnt +=  ​1
                if cnt > best_score or (cnt == best_score and deg[i] > best_deg):
                    best_score = cnt
                    best_deg = deg[i]
                    best = i
        if best == -1:
            return True

        # Try colors 1,2,3
        used = [False] * 4
        for nb in adj[best]:
            if color[nb] != 0:
                used[color[nb]] = True

        for c in range(1, 4):
            if not used[c]:
                color[best] = c
                if backtrack():
                    return True
                color[best] =  ​0
        return False

    if backtrack():
        print("YES")
        print(" ".join(map(str, color))))
    else:
        print("NO")

if __name__ == "__main__":
    solve()