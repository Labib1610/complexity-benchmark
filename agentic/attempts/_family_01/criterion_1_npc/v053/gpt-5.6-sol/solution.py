import sys
sys.setrecursionlimit(1000000)

def solve_component(vertices, global_adj):
    k = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    adj = [0] * k
    edges = []

    for i, v in enumerate(vertices):
        mask = 0
        for u in global_adj[v]:
            j = index.get(u)
            if j is not None:
                mask |= 1 << j
                if i < j:
                    edges.append((i, j))
        adj[i] = mask

    # Bipartite components need only two colors.
    bip_color = [-1] * k
    bipartite = True
    for start in range(k):
        if bip_color[start] != -1:
            continue
        bip_color[start] = 0
        queue = [start]
        for v in queue:
            nb = adj[v]
            while nb:
                bit = nb & -nb
                u = bit.bit_length() - 1
                nb -= bit
                if bip_color[u] == -1:
                    bip_color[u] = bip_color[v] ^ 1
                    queue.append(u)
                elif bip_color[u] == bip_color[v]:
                    bipartite = False
                    break
            if not bipartite:
                break
        if not bipartite:
            break

    if bipartite:
        return [1 << c for c in bip_color]

    triangles = []
    for i in range(k):
        nb = adj[i] & ~((1 << (i + 1)) - 1)
        while nb:
            bj = nb & -nb
            j = bj.bit_length() - 1
            nb -= bj
            common = adj[i] & adj[j] & ~((1 << (j + 1)) - 1)
            while common:
                bk = common & -common
                triangles.append((i, j, bk.bit_length() - 1))
                common -= bk

    def propagate(dom):
        processed = [False] * k
        queue = [i for i in range(k) if dom[i] & (dom[i] - 1) == 0]
        head = 0

        while True:
            while head < len(queue):
                v = queue[head]
                head += 1
                if processed[v]:
                    continue
                if dom[v] == 0:
                    return False
                processed[v] = True
                color = dom[v]

                nb = adj[v]
                while nb:
                    bit = nb & -nb
                    u = bit.bit_length() - 1
                    nb -= bit
                    if dom[u] & color:
                        nd = dom[u] & ~color
                        if nd == 0:
                            return False
                        if nd != dom[u]:
                            dom[u] = nd
                            if nd & (nd - 1) == 0:
                                queue.append(u)

            changed = False
            for a, b, c in triangles:
                da, db, dc = dom[a], dom[b], dom[c]
                if (da | db | dc).bit_count() < 3:
                    return False

                pairs = ((a, b, c), (a, c, b), (b, c, a))
                for x, y, z in pairs:
                    union = dom[x] | dom[y]
                    cnt = union.bit_count()
                    if cnt < 2:
                        return False
                    if cnt == 2:
                        nd = dom[z] & ~union
                        if nd == 0:
                            return False
                        if nd != dom[z]:
                            dom[z] = nd
                            changed = True
                            if nd & (nd - 1) == 0 and not processed[z]:
                                queue.append(z)

            if head < len(queue):
                continue
            if not changed:
                return True

    def solve_two_sat(dom):
        variables = []
        var_id = [-1] * k
        options = []

        for v in range(k):
            if dom[v].bit_count() == 2:
                var_id[v] = len(variables)
                variables.append(v)
                bits = []
                mask = dom[v]
                while mask:
                    bit = mask & -mask
                    bits.append(bit)
                    mask -= bit
                options.append(bits)

        t = len(variables)
        if t == 0:
            return dom[:]

        graph = [[] for _ in range(2 * t)]
        reverse = [[] for _ in range(2 * t)]

        def add_implication(a, b):
            graph[a].append(b)
            reverse[b].append(a)

        for u, v in edges:
            du, dv = dom[u], dom[v]
            common = du & dv
            while common:
                color = common & -common
                common -= color

                iu = var_id[u]
                iv = var_id[v]

                if iu == -1 and iv == -1:
                    return None
                elif iu == -1:
                    if du == color:
                        j = 0 if options[iv][0] == color else 1
                        # Forbid variable iv choosing j.
                        add_implication(2 * iv + j, 2 * iv + (1 - j))
                elif iv == -1:
                    if dv == color:
                        i = 0 if options[iu][0] == color else 1
                        add_implication(2 * iu + i, 2 * iu + (1 - i))
                else:
                    i = 0 if options[iu][0] == color else 1
                    j = 0 if options[iv][0] == color else 1
                    add_implication(2 * iu + i, 2 * iv + (1 - j))
                    add_implication(2 * iv + j, 2 * iu + (1 - i))

        seen = [False] * (2 * t)
        order = []

        for start in range(2 * t):
            if seen[start]:
                continue
            seen[start] = True
            stack = [(start, 0)]
            while stack:
                v, p = stack[-1]
                if p < len(graph[v]):
                    u = graph[v][p]
                    stack[-1] = (v, p + 1)
                    if not seen[u]:
                        seen[u] = True
                        stack.append((u, 0))
                else:
                    order.append(v)
                    stack.pop()

        comp = [-1] * (2 * t)
        cid = 0
        for start in reversed(order):
            if comp[start] != -1:
                continue
            comp[start] = cid
            stack = [start]
            while stack:
                v = stack.pop()
                for u in reverse[v]:
                    if comp[u] == -1:
                        comp[u] = cid
                        stack.append(u)
            cid += 1

        result = dom[:]
        for j, v in enumerate(variables):
            n0 = 2 * j
            n1 = n0 + 1
            if comp[n0] == comp[n1]:
                return None
            choice = 1 if comp[n1] > comp[n0] else 0
            result[v] = options[j][choice]

        return result

    failed = set()
    CACHE_LIMIT = 250000

    def canonical_key(dom):
        key = tuple(dom)
        swapped = tuple((x & 1) | ((x & 2) << 1) | ((x & 4) >> 1) for x in dom)
        return key if key <= swapped else swapped

    def search(dom):
        if not propagate(dom):
            return None

        key = canonical_key(dom)
        if key in failed:
            return None

        branch_vertex = -1
        best_score = (-1, -1, -1)

        for v in range(k):
            if dom[v] == 7:
                unrestrained_neighbors = 0
                non_single_neighbors = 0
                nb = adj[v]
                while nb:
                    bit = nb & -nb
                    u = bit.bit_length() - 1
                    nb -= bit
                    if dom[u] == 7:
                        unrestrained_neighbors += 1
                    if dom[u].bit_count() > 1:
                        non_single_neighbors += 1
                score = (unrestrained_neighbors, non_single_neighbors, adj[v].bit_count())
                if score > best_score:
                    best_score = score
                    branch_vertex = v

        if branch_vertex == -1:
            result = solve_two_sat(dom)
            if result is not None:
                return result
            if len(failed) < CACHE_LIMIT:
                failed.add(key)
            return None

        colors = [1, 2, 4]
        colors.sort(key=lambda color: sum(
            1 for u in range(k)
            if ((adj[branch_vertex] >> u) & 1) and (dom[u] & color)
        ))

        for color in colors:
            nd = dom[:]
            nd[branch_vertex] = color
            result = search(nd)
            if result is not None:
                return result

        if len(failed) < CACHE_LIMIT:
            failed.add(key)
        return None

    anchor = max(range(k), key=lambda v: adj[v].bit_count())
    initial = [7] * k
    initial[anchor] = 1
    return search(initial)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    global_adj = [set() for _ in range(n)]
    impossible = False

    p = 2
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u == v:
            impossible = True
        else:
            global_adj[u].add(v)
            global_adj[v].add(u)

    if impossible:
        print("NO")
        return

    visited = [False] * n
    answer = [0] * n

    for start in range(n):
        if visited[start]:
            continue

        visited[start] = True
        component = [start]
        queue = [start]

        for v in queue:
            for u in global_adj[v]:
                if not visited[u]:
                    visited[u] = True
                    component.append(u)
                    queue.append(u)

        result = solve_component(component, global_adj)
        if result is None:
            print("NO")
            return

        for local, vertex in enumerate(component):
            answer[vertex] = result[local].bit_length()

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()