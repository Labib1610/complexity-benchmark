import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    nL = next(it)
    nR = next(it)
    m = next(it)

    left_vertex = [0] * m
    right_vertex = [0] * m
    deg_left = [0] * (nL + 1)
    deg_right = [0] * (nR + 1)

    for i in range(m):
        u = next(it)
        v = next(it)
        left_vertex[i] = u
        right_vertex[i] = v
        deg_left[u] += 1
        deg_right[v] +=  ​1

    Delta = max(max(deg_left, default=0), max(deg_right, default=0)

    if m == 0:
        sys.stdout.write("YES\n\n")
        return

    used_left = [set() for _ in range(nL + 1)]
    used_right = [set() for _ in range(nR + 1)]
    color_to_left = [None] * (nL +  ​1)
    color_to_right = [None] * (nR +  ​1)
    color = [0] * m

    next_free_left = [1] * (nL +  ​1)
    next_free_right = [1] * (nR +  ​1)

    def set_color(eid, c):
        u = left_vertex[eid]
        v = right_vertex[eid]

        if color_to_left[u] is None:
            color_to_left[u] = {}
        if color_to_right[v] is None:
            color_to_right[v] = {}

        color_to_left[u][c] = (v, eid)
        color_to_right[v][c] = (u, eid)
        used_left[u].add(c)
        used_right[v].add(c)

        if c == next_free_left[u]:
            while next_free_left[u] in used_left[u]:
                next_free_left[u] += 1
        if c == next_free_right[v]:
            while next_free_right[v] in used_right[v]:
                next_free_right[v] += 1

        color[eid] = c

    def recolor_edge(eid, new_c):
        old_c = color[eid]
        if old_c == new_c:
            return

        u = left_vertex[eid]
        v = right_vertex[eid]

        # remove old color
        del color_to_left[u][old_c]
        del color_to_right[v][old_c]
        used_left[u].remove(old_c)
        used_right[v].remove(old_c)

        if old_c < next_free_left[u]:
            next_free_left[u] = old_c
        if old_c < next_free_right[v]:
            next_free_right[v] = old_c

        # add new color
        if color_to_left[u] is None:
            color_to_left[u] = {}
        if color_to_right[v] is None:
            color_to_right[v] = {}

        color_to_left[u][new_c] = (v, eid)
        color_to_right[v][new_c] = (u, eid)
        used_left[u].add(new_c)
        used_right[v].add(new_c)

        if new_c == next_free_left[u]:
            while next_free_left[u] in used_left[u]:
                next_free_left[u] += 1
        if new_c == next_free_right[v]:
            while next_free_right[v] in used_right[v]:
                next_free_right[v] += 1

        color[eid] = new_c

    for eid in range(m):
        u = left_vertex[eid]
        v = right_vertex[eid]

        # smallest color free at both u and v
        c = max(next_free_left[u], next_free_right[v])
        while c in used_left[u] or c in used_right[v]:
            c += 1

        if c <= Delta:
            set_color(eid, c)
        else:
            # a in S_u \ S_v
            a = 1
            while a in used_right[v] or a not in used_left[u]:
                a += 1

            # b in S_v \ S_u
            b = 1
            while b in used_left[u] or b not in used_right[v]:
                b += 1

            # alternating path starting at v with color b
            cur = v
            from_col = b
            to_col = a
            path_edges = []
            path_new_colors = []

            while True:
                if cur <= nL:
                    used_cur = used_left[cur]
                    color_to_cur = color_to_left[cur]
                else:
                    used_cur = used_right[cur]
                    color_to_cur = color_to_right[cur]

                if from_col not in used_cur:
                    break

                nxt, eid2 = color_to_cur[from_col]
                path_edges.append(eid2)
                path_new_colors.append(to_col)

                cur = nxt
                from_col, to_col = to_col, from_col

            # recolor the path
            for eid2, new_c in zip(path_edges, path_new_colors):
                recolor_edge(eid2, new_c)

            # assign b to the new edge
            set_color(eid, b)

    out = ["YES"]
    out.append(" ".join(map(str, color)))
    sys.stdout.write("\n".join(out) + "\n"

if __name__ == "__main__":
    main()