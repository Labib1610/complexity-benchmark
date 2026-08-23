import sys

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if v not in adj[u]:
            adj[u].append(v)
            adj[v].append(u)

    color = [0] * (n + 1)          # 0 = uncolored, 1/2/3 = colors
    counts = [[0, 0, 0] for _ in range(n + 1)]  # counts of neighbor colors

    sys.setrecursionlimit(10000)

    def dfs(idx):
        if idx > n:
            return True
        for c in (1, 2, 3):
            # check direct conflicts
            conflict = False
            for nb in adj[idx]:
                if color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue

            # assign color
            color[idx] = c
            for nb in adj[idx]:
                counts[nb][c - 1] += 1

            # forward checking on neighbors of idx
            fail = False
            for nb in adj[idx]:
                if color[nb] == 0:
                    if counts[nb][0] > 0 and counts[nb][1] > 0 and counts[nb][2] > 0:
                        fail = True
                        break

            if not fail:
                if dfs(idx + 1):
                    return True

            # undo assignment
            for nb in adj[idx]:
                counts[nb][c - 1] -= 1
            color[idx] = 0

        return False

    if dfs(1):
        out = ['YES', '\n', ' '.join(str(color[i]) for i in range(1, n + 1))]
        sys.stdout.write(''.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    main()