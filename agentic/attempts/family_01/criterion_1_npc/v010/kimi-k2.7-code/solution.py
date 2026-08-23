import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n)]
    adj_mask = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    full_mask = (1 << n) - 1

    # masks of vertices assigned to each color (1->c1, 2->c2, 3->c3)
    c1 = c2 = c3 = 0
    answer = [0] * n

    def feasible(idx: int, col: int) -> bool:
        nonlocal c1, c2, c3
        if col == 1:
            # color-1 set must stay independent
            if adj_mask[idx] & c1:
                return False
            new_c1 = c1 | (1 << idx)
            new_c2 = c2
            new_c3 = c3
        elif col == 2:
            new_c1 = c1
            new_c2 = c2 | (1 << idx)
            new_c3 = c3
        else:
            new_c1 = c1
            new_c2 = c2
            new_c3 = c3 | (1 << idx)

        # vertices not in color 1 must be 2-colored (colors 2 and 3)
        R = full_mask ^ new_c1
        side = [-1] * n

        mm = new_c2
        while mm:
            lsb = mm & -mm
            v = lsb.bit_length() - 1
            side[v] = 0
            mm ^= lsb
        mm = new_c3
        while mm:
            lsb = mm & -mm
            v = lsb.bit_length() - 1
            side[v] = 1
            mm ^= lsb

        visited = [False] * n

        # start BFS from every precolored vertex
        for v in range(n):
            if (R >> v) & 1 and side[v] != -1 and not visited[v]:
                visited[v] = True
                stack = [v]
                while stack:
                    x = stack.pop()
                    for y in adj[x]:
                        if not ((R >> y) & 1):
                            continue
                        if not visited[y]:
                            if side[y] == -1:
                                side[y] = side[x] ^ 1
                            elif side[y] == side[x]:
                                return False
                            visited[y] = True
                            stack.append(y)
                        else:
                            if side[y] == side[x]:
                                return False

        # components without precolored vertices
        for v in range(n):
            if (R >> v) & 1 and side[v] == -1 and not visited[v]:
                side[v] = 0
                visited[v] = True
                stack = [v]
                while stack:
                    x = stack.pop()
                    for y in adj[x]:
                        if not ((R >> y) & 1):
                            continue
                        if not visited[y]:
                            side[y] = side[x] ^ 1
                            visited[y] = True
                            stack.append(y)
                        else:
                            if side[y] == side[x]:
                                return False
        return True

    for i in range(n):
        chosen = 0
        for col in (1, 2, 3):
            if feasible(i, col):
                chosen = col
                break
        if chosen == 0:
            sys.stdout.write("NO")
            return
        answer[i] = chosen
        if chosen == 1:
            c1 |= 1 << i
        elif chosen == 2:
            c2 |= 1 << i
        else:
            c3 |= 1 << i

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, answer)))

if __name__ == "__main__":
    solve()