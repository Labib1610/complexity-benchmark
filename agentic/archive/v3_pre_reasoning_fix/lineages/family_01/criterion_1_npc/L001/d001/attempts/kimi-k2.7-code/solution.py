import sys

def solve_component(k, neigh):
    if k == 0:
        return []
    if k == 1:
        return [0]

    color = [-1] * k
    avail = [7] * k   # bits 0,1,2 correspond to frequencies 1,2,3

    sys.setrecursionlimit(10000)

    def dfs(pos):
        while pos < k and color[pos] != -1:
            pos += 1
        if pos == k:
            return True

        v = pos
        mask = avail[v]

        for c in range(3):
            if not ((mask >> c) & 1):
                continue

            assigned = [v]
            changed = []
            color[v] = c
            stack = [v]
            ok = True

            while stack and ok:
                x = stack.pop()
                col = color[x]
                for u in neigh[x]:
                    if color[u] != -1:
                        continue
                    a = avail[u]
                    if (a >> col) & 1:
                        new = a & ~(1 << col)
                        avail[u] = new
                        changed.append((u, a))
                        if new == 0:
                            ok = False
                            break
                        # single remaining color -> forced assignment
                        if new & (new - 1) == 0:
                            cu = new.bit_length() - 1
                            color[u] = cu
                            assigned.append(u)
                            stack.append(u)

            if ok:
                if dfs(pos + 1):
                    return True

            # undo assignments and availability changes
            for u, old in changed:
                avail[u] = old
            for u in assigned:
                color[u] = -1

        return False

    if dfs(0):
        return color
    return None


def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            print("NO")
            return
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    visited = [False] * n
    ans = [0] * n
    global_to_local = [-1] * n

    for i in range(n):
        if visited[i]:
            continue

        # collect connected component
        stack = [i]
        visited[i] = True
        comp = []
        while stack:
            x = stack.pop()
            comp.append(x)
            mask = adj[x]
            while mask:
                lsb = mask & -mask
                y = lsb.bit_length() - 1
                if not visited[y]:
                    visited[y] = True
                    stack.append(y)
                mask ^= lsb

        comp.sort()
        k = len(comp)

        for j, v in enumerate(comp):
            global_to_local[v] = j

        neigh = [[] for _ in range(k)]
        for j, v in enumerate(comp):
            mask = adj[v]
            while mask:
                lsb = mask & -mask
                y = lsb.bit_length() - 1
                neigh[j].append(global_to_local[y])
                mask ^= lsb

        colors = solve_component(k, neigh)
        if colors is None:
            print("NO")
            return

        for j, v in enumerate(comp):
            ans[v] = colors[j] + 1
            global_to_local[v] = -1

    print("YES")
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    solve()