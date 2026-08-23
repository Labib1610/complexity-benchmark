import sys
sys.setrecursionlimit(1000000)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbors = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u

    color_masks = [0, 0, 0, 0]  # index 1..3
    assignment = [0] * n
    found = False

    def dfs(idx):
        nonlocal found
        if idx == n:
            found = True
            return True
        node = idx
        neigh = neighbors[node]
        for col in (1, 2, 3):
            if neigh & color_masks[col]:
                continue
            assignment[node] = col
            color_masks[col] |= 1 << node
            if dfs(idx + 1):
                return True
            color_masks[col] &= ~(1 << node)
            assignment[node] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(assignment[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    main()