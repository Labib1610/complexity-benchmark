import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neigh_before = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u > v:
            u, v = v, u
        # u < v
        neigh_before[v].append(u)
        neigh_before[u].append(v)  # will ignore when checking for j < i

    assignment = [0] * n
    sys.setrecursionlimit(10000)

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        for color in (1, 2, 3):
            conflict = False
            for j in neigh_before[idx]:
                if j < idx and assignment[j] == color:
                    conflict = True
                    break
            if conflict:
                continue
            assignment[idx] = color
            if dfs(idx + 1):
                return True
        assignment[idx] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(map(str, assignment))]
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()