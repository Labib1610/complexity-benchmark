import sys

sys.setrecursionlimit(10000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj_sets = [set() for _ in range(n)]
    p = 2
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u != v:
            adj_sets[u].add(v)
            adj_sets[v].add(u)

    adj = [list(s) for s in adj_sets]
    adj_mask = [0] * n
    for v in range(n):
        mask = 0
        for u in adj[v]:
            mask |= 1 << u
        adj_mask[v] = mask

    # A K4 is immediately not 3-colorable.
    for u in range(n):
        candidates = adj_mask[u] & ~((1 << (u + 1)) - 1)
        x = candidates
        while x:
            vb = x & -x
            v = vb.bit_length() - 1
            common = candidates & adj_mask[v] & ~((1 << (v + 1)) - 1)
            y = common
            while y:
                wb = y & -y
                w = wb.bit_length() - 1
                if adj_mask[w] & common & ~((1 << (w + 1)) - 1):
                    print("NO")
                    return
                y -= wb
            x -= vb

    def solve(fixed, preferred=None):
        domains = [7] * n
        queue = []

        for v, color in enumerate(fixed):
            bit = 1 << (color - 1)
            domains[v] = bit
            queue.append(v)

        def initial_propagate():
            head = 0
            while head < len(queue):
                v = queue[head]
                head += 1
                bit = domains[v]
                if bit == 0 or bit & (bit - 1):
                    continue
                for u in adj[v]:
                    if domains[u] & bit:
                        nd = domains[u] & ~bit
                        if nd == 0:
                            return False
                        if nd != domains[u]:
                            domains[u] = nd
                            if nd & (nd - 1) == 0:
                                queue.append(u)
            return True

        if not initial_propagate():
            return None

        failed = set()
        memo_limit = 50000

        def solve_binary_component(component):
            k = len(component)
            index = {v: i for i, v in enumerate(component)}
            size = 2 * k
            graph = [[] for _ in range(size)]
            reverse = [[] for _ in range(size)]
            options = []

            for v in component:
                bits = []
                x = domains[v]
                while x:
                    b = x & -x
                    bits.append(b)
                    x -= b
                if len(bits) != 2:
                    return None
                options.append(bits)

            def add_implication(a, b):
                graph[a].append(b)
                reverse[b].append(a)

            comp_set = set(component)
            for v in component:
                iv = index[v]
                for u in adj[v]:
                    if u not in comp_set or v >= u:
                        continue
                    iu = index[u]
                    for ov in range(2):
                        for ou in range(2):
                            if options[iv][ov] == options[iu][ou]:
                                a = 2 * iv + ov
                                b = 2 * iu + ou
                                add_implication(a, b ^ 1)
                                add_implication(b, a ^ 1)

            seen = [False] * size
            order = []

            def dfs1(start):
                stack = [(start, 0)]
                seen[start] = True
                while stack:
                    v, i = stack[-1]
                    if i < len(graph[v]):
                        u = graph[v][i]
                        stack[-1] = (v, i + 1)
                        if not seen[u]:
                            seen[u] = True
                            stack.append((u, 0))
                    else:
                        order.append(v)
                        stack.pop()

            for v in range(size):
                if not seen[v]:
                    dfs1(v)

            scc = [-1] * size
            cid = 0
            for start in reversed(order):
                if scc[start] != -1:
                    continue
                scc[start] = cid
                stack = [start]
                while stack:
                    v = stack.pop()
                    for u in reverse[v]:
                        if scc[u] == -1:
                            scc[u] = cid
                            stack.append(u)
                cid += 1

            chosen = []
            for i in range(k):
                if scc[2 * i] == scc[2 * i + 1]:
                    return None
                choice = 0 if scc[2 * i] > scc[2 * i + 1] else 1
                chosen.append(options[i][choice])
            return chosen

        def recurse():
            key = tuple(domains)
            if key in failed:
                return False

            unresolved = [v for v in range(n) if domains[v] & (domains[v] - 1)]
            if not unresolved:
                return True

            v = min(
                unresolved,
                key=lambda x: (
                    domains[x].bit_count(),
                    -sum(1 for u in adj[x] if domains[u] & (domains[u] - 1)),
                    -len(adj[x]),
                )
            )

            component = []
            seen_mask = 1 << v
            stack = [v]
            all_binary = True
            while stack:
                x = stack.pop()
                component.append(x)
                if domains[x].bit_count() != 2:
                    all_binary = False
                for u in adj[x]:
                    if domains[u] & (domains[u] - 1) and not (seen_mask >> u) & 1:
                        seen_mask |= 1 << u
                        stack.append(u)

            if all_binary:
                chosen = solve_binary_component(component)
                if chosen is None:
                    if len(failed) < memo_limit:
                        failed.add(key)
                    return False

                old = [(x, domains[x]) for x in component]
                for x, bit in zip(component, chosen):
                    domains[x] = bit

                if recurse():
                    return True

                for x, value in old:
                    domains[x] = value

                if len(failed) < memo_limit:
                    failed.add(key)
                return False

            bits = []
            x = domains[v]
            while x:
                bit = x & -x
                bits.append(bit)
                x -= bit

            if preferred is not None:
                pref_bit = 1 << (preferred[v] - 1)
                if pref_bit in bits:
                    bits.remove(pref_bit)
                    bits.insert(0, pref_bit)

            for bit in bits:
                trail = []

                def change(vertex, new_domain):
                    if domains[vertex] != new_domain:
                        trail.append((vertex, domains[vertex]))
                        domains[vertex] = new_domain

                change(v, bit)
                q = [v]
                head = 0
                valid = True

                while head < len(q) and valid:
                    x = q[head]
                    head += 1
                    xb = domains[x]
                    for u in adj[x]:
                        if domains[u] & xb:
                            nd = domains[u] & ~xb
                            if nd == 0:
                                valid = False
                                break
                            if nd != domains[u]:
                                change(u, nd)
                                if nd & (nd - 1) == 0:
                                    q.append(u)

                if valid and recurse():
                    return True

                for vertex, old_domain in reversed(trail):
                    domains[vertex] = old_domain

            if len(failed) < memo_limit:
                failed.add(key)
            return False

        if not recurse():
            return None
        return [d.bit_length() for d in domains]

    answer = solve([1])
    if answer is None:
        print("NO")
        return

    for i in range(1, n):
        current = answer[i]
        for color in range(1, current):
            candidate = solve(answer[:i] + [color], answer)
            if candidate is not None:
                answer = candidate
                break

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()