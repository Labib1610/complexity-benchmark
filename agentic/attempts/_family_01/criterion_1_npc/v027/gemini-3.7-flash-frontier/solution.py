import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    adj_sets = [set() for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        if u == v:
            print("NO")
            return
        adj_sets[u].add(v)
        adj_sets[v].add(u)

    adj = [list(adj_sets[i]) for i in range(n)]
    deg = [len(adj[i]) for i in range(n)]

    color = [-1] * n
    avail = [7] * n  # bitmask of available colors (1: color 0, 2: color 1, 4: color 2)
    popcnt = [0, 1, 1, 2, 1, 2, 2, 3]

    def dfs(unassigned_count):
        if unassigned_count == 0:
            return True

        best_u = -1
        min_c = 4
        max_d = -1
        for u in range(n):
            if color[u] == -1:
                cnt = popcnt[avail[u]]
                if cnt == 0:
                    return False
                if cnt < min_c or (cnt == min_c and deg[u] > max_d):
                    min_c = cnt
                    max_d = deg[u]
                    best_u = u
                    if min_c == 1:
                        break

        u = best_u
        u_avail = avail[u]

        for c in range(3):
            if (u_avail >> c) & 1:
                color[u] = c
                changed = []
                c_mask = ~(1 << c)
                possible = True
                for v in adj[u]:
                    if color[v] == -1:
                        if (avail[v] >> c) & 1:
                            changed.append(v)
                            avail[v] &= c_mask
                            if avail[v] == 0:
                                possible = False

                if possible and dfs(unassigned_count - 1):
                    return True

                for v in changed:
                    avail[v] |= 1 << c
                color[u] = -1

        return False

    if dfs(n):
        print("YES")
        print(*(color[i] + 1 for i in range(n)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()