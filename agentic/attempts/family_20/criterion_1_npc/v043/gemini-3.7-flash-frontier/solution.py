import sys

# Increase recursion depth for deep search trees
sys.setrecursionlimit(50000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    edges = []
    adj_v = [[] for _ in range(n)]
    idx = 2
    for i in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        edges.append((u, v))
        adj_v[u].append(i)
        adj_v[v].append(i)

    color = [-1] * m
    v_mask = [0] * n
    colored_count = [0] * n
    history = []

    def try_assign(e, c, queue):
        u, v = edges[e]
        mask = 1 << c
        if (v_mask[u] & mask) or (v_mask[v] & mask):
            return False

        color[e] = c
        v_mask[u] |= mask
        v_mask[v] |= mask
        colored_count[u] += 1
        colored_count[v] += 1
        history.append(e)

        if colored_count[u] == 2:
            rem_mask = 7 ^ v_mask[u]
            rem_c = (
                0
                if rem_mask == 1
                else (1 if rem_mask == 2 else 2)
            )
            for ne in adj_v[u]:
                if color[ne] == -1:
                    queue.append((ne, rem_c))
                    break

        if colored_count[v] == 2:
            rem_mask = 7 ^ v_mask[v]
            rem_c = (
                0
                if rem_mask == 1
                else (1 if rem_mask == 2 else 2)
            )
            for ne in adj_v[v]:
                if color[ne] == -1:
                    queue.append((ne, rem_c))
                    break

        return True

    def undo_to(checkpoint):
        while len(history) > checkpoint:
            e = history.pop()
            c = color[e]
            u, v = edges[e]
            mask = 1 << c
            v_mask[u] &= ~mask
            v_mask[v] &= ~mask
            colored_count[u] -= 1
            colored_count[v] -= 1
            color[e] = -1

    def search():
        if len(history) == m:
            return True

        # Pick the most constrained uncolored edge
        best_e = -1
        best_score = -1
        for e in range(m):
            if color[e] == -1:
                u, v = edges[e]
                score = colored_count[u] + colored_count[v]
                if score > best_score:
                    best_score = score
                    best_e = e
                    if score == 2:
                        break

        if best_e == -1:
            return True

        u, v = edges[best_e]
        used = v_mask[u] | v_mask[v]
        available_colors = [c for c in range(3) if not (used & (1 << c))]

        for c in available_colors:
            checkpoint = len(history)
            queue = []
            if try_assign(best_e, c, queue):
                conflict = False
                q_idx = 0
                while q_idx < len(queue):
                    ne, nc = queue[q_idx]
                    q_idx += 1
                    if color[ne] != -1:
                        if color[ne] != nc:
                            conflict = True
                            break
                    else:
                        if not try_assign(ne, nc, queue):
                            conflict = True
                            break

                if not conflict:
                    if search():
                        return True

            undo_to(checkpoint)

        return False

    if search():
        print("YES")
        print(*(color[i] + 1 for i in range(m)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()