import sys

def main():
    sys.setrecursionlimit(1000000)
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

    assignment = [0] * n  # 0 means uncolored

    def dfs(idx):
        if idx == n:
            return True
        for color in (1, 2, 3):
            conflict = False
            for nb in adj[idx]:
                if assignment[nb] == color:
                    conflict = True
                    break
            if conflict:
                continue
            assignment[idx] = color
            # Forward checking
            fail = False
            for j in range(idx + 1, n):
                used = set()
                for nb in adj[j]:
                    c = assignment[nb]
                    if c:
                        used.add(c)
                        if len(used) == 3:
                            fail = True
                            break
                if fail:
                    break
            if not fail:
                if dfs(idx + 1):
                    return True
            assignment[idx] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(c) for c in assignment))
    else:
        print("NO")

if __name__ == "__main__":
    main()