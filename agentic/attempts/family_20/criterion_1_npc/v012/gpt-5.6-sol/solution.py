import sys
import heapq

sys.setrecursionlimit(1000000)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    edges = []
    adj = [[] for _ in range(n)]
    p = 2

    for eid in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        edges.append((u, v))
        if 0 <= u < n and 0 <= v < n:
            adj[u].append(eid)
            adj[v].append(eid)

    if m * 2 != 3 * n or any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # Find connected components, bipartitions, and bridges.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False
    components = []

    def dfs_bridge(v, parent_edge, comp):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1
        comp.append(v)

        for eid in adj[v]:
            a, b = edges[eid]
            to = b if a == v else a
            if eid == parent_edge:
                continue
            if tin[to] == -1:
                dfs_bridge(to, eid, comp)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True
            else:
                low[v] = min(low[v], tin[to])

    for start in range(n):
        if tin[start] == -1:
            comp = []
            dfs_bridge(start, -1, comp)
            components.append(comp)

    if has_bridge:
        print("NO")
        return

    answer = [-1] * m
    non_bip_components = []

    # Directly color bipartite cubic components.
    for comp in components:
        side = {comp[0]: 0}
        stack = [comp[0]]
        bipartite = True

        while stack:
            v = stack.pop()
            for eid in adj[v]:
                a, b = edges[eid]
                to = b if a == v else a
                if to not in side:
                    side[to] = side[v] ^ 1
                    stack.append(to)
                elif side[to] == side[v]:
                    bipartite = False

        if not bipartite:
            non_bip_components.append(comp)
            continue

        left = [v for v in comp if side[v] == 0]
        match_right = {}
        stamp = {}
        current_stamp = 0

        def augment(u):
            nonlocal current_stamp
            for eid in adj[u]:
                a, b = edges[eid]
                v = b if a == u else a
                if stamp.get(v, -1) == current_stamp:
                    continue
                stamp[v] = current_stamp

                old = match_right.get(v, -1)
                if old == -1:
                    match_right[v] = eid
                    return True

                x, y = edges[old]
                old_left = x if side[x] == 0 else y
                if augment(old_left):
                    match_right[v] = eid
                    return True
            return False

        possible = True
        for u in left:
            current_stamp += 1
            if not augment(u):
                possible = False
                break

        if not possible:
            print("NO")
            return

        matching_edges = set(match_right.values())
        for eid in matching_edges:
            answer[eid] = 0

        # The remaining edges form disjoint even cycles.
        for v in comp:
            for start_eid in adj[v]:
                if answer[start_eid] != -1:
                    continue

                answer[start_eid] = 1
                queue = [start_eid]
                qi = 0

                while qi < len(queue):
                    eid = queue[qi]
                    qi += 1
                    color = answer[eid]
                    a, b = edges[eid]

                    for x in (a, b):
                        for other in adj[x]:
                            if other == eid or answer[other] == 0:
                                continue
                            needed = 3 - color  # 1 <-> 2
                            if answer[other] == -1:
                                answer[other] = needed
                                queue.append(other)
                            elif answer[other] != needed:
                                print("NO")
                                return

    if not non_bip_components:
        print("YES")
        print(*[x + 1 for x in answer])
        return

    # SAT encoding for the remaining components.
    # Variable (edge, color): edge * 3 + color + 1.
    num_vars = 3 * m
    clauses = []
    unit_literals = []
    activity = [0.0] * (num_vars + 1)

    def add_clause(clause):
        cid = len(clauses)
        clauses.append(clause)
        for lit in clause:
            activity[abs(lit)] += 1.0
        return cid

    for eid in range(m):
        x = 3 * eid + 1
        add_clause([x, x + 1, x + 2])
        add_clause([-x, -(x + 1)])
        add_clause([-x, -(x + 2)])
        add_clause([-(x + 1), -(x + 2)])

    for v in range(n):
        inc = adj[v]
        for i in range(3):
            for j in range(i + 1, 3):
                e1 = inc[i]
                e2 = inc[j]
                for color in range(3):
                    add_clause([-(3 * e1 + color + 1),
                                -(3 * e2 + color + 1)])

    # Fix already colored bipartite components.
    for eid, color in enumerate(answer):
        if color != -1:
            unit_literals.append(3 * eid + color + 1)

    # Remove the global color symmetry independently in every uncolored component.
    for comp in non_bip_components:
        v = comp[0]
        for color, eid in enumerate(adj[v]):
            unit_literals.append(3 * eid + color + 1)

    watches = [[] for _ in range(2 * num_vars + 1)]

    def widx(lit):
        return lit + num_vars

    for cid, clause in enumerate(clauses):
        if len(clause) >= 2:
            watches[widx(clause[0])].append(cid)
            watches[widx(clause[1])].append(cid)

    assignment = [-1] * (num_vars + 1)
    level = [0] * (num_vars + 1)
    reason = [-1] * (num_vars + 1)
    trail = []
    trail_lim = []
    qhead = 0
    heap = [(-activity[v], v) for v in range(1, num_vars + 1)]
    heapq.heapify(heap)
    var_inc = 1.0

    def lit_value(lit):
        val = assignment[abs(lit)]
        if val == -1:
            return -1
        return val if lit > 0 else 1 - val

    def enqueue(lit, why):
        v = abs(lit)
        wanted = 1 if lit > 0 else 0
        if assignment[v] != -1:
            return assignment[v] == wanted
        assignment[v] = wanted
        level[v] = len(trail_lim)
        reason[v] = why
        trail.append(lit)
        return True

    def propagate():
        nonlocal qhead
        while qhead < len(trail):
            p_lit = trail[qhead]
            qhead += 1
            false_lit = -p_lit
            ws = watches[widx(false_lit)]
            i = 0

            while i < len(ws):
                cid = ws[i]
                clause = clauses[cid]

                if clause[0] == false_lit:
                    wi, oi = 0, 1
                elif clause[1] == false_lit:
                    wi, oi = 1, 0
                else:
                    ws[i] = ws[-1]
                    ws.pop()
                    continue

                other = clause[oi]
                if lit_value(other) == 1:
                    i += 1
                    continue

                replacement = -1
                for k in range(2, len(clause)):
                    if lit_value(clause[k]) != 0:
                        replacement = k
                        break

                if replacement != -1:
                    new_lit = clause[replacement]
                    clause[wi], clause[replacement] = new_lit, false_lit
                    ws[i] = ws[-1]
                    ws.pop()
                    watches[widx(new_lit)].append(cid)
                    continue

                other_value = lit_value(other)
                if other_value == 0:
                    return cid

                if not enqueue(other, cid):
                    return cid
                i += 1

        return -1

    def backtrack(target_level):
        nonlocal qhead
        if len(trail_lim) <= target_level:
            return

        start = trail_lim[target_level]
        for i in range(len(trail) - 1, start - 1, -1):
            v = abs(trail[i])
            assignment[v] = -1
            level[v] = 0
            reason[v] = -1
            heapq.heappush(heap, (-activity[v], v))

        del trail[start:]
        del trail_lim[target_level:]
        qhead = min(qhead, len(trail))

    seen = [False] * (num_vars + 1)

    def analyze(conflict_cid):
        nonlocal var_inc
        learned = [0]
        touched = []
        path_count = 0
        idx = len(trail) - 1
        p_lit = 0
        clause = clauses[conflict_cid]
        current_level = len(trail_lim)

        while True:
            pv = abs(p_lit)
            for q in clause:
                v = abs(q)
                if v == pv or seen[v] or level[v] == 0:
                    continue
                seen[v] = True
                touched.append(v)

                activity[v] += var_inc
                heapq.heappush(heap, (-activity[v], v))

                if activity[v] > 1e100:
                    for x in range(1, num_vars + 1):
                        activity[x] *= 1e-100
                    var_inc *= 1e-100

                if level[v] == current_level:
                    path_count += 1
                else:
                    learned.append(q)

            while idx >= 0 and not seen[abs(trail[idx])]:
                idx -= 1

            p_lit = trail[idx]
            idx -= 1
            path_count -= 1

            if path_count == 0:
                learned[0] = -p_lit
                break

            r = reason[abs(p_lit)]
            clause = clauses[r]

        back_level = 0
        if len(learned) > 1:
            best = 1
            for i in range(2, len(learned)):
                if level[abs(learned[i])] > level[abs(learned[best])]:
                    best = i
            learned[1], learned[best] = learned[best], learned[1]
            back_level = level[abs(learned[1])]

        for v in touched:
            seen[v] = False

        var_inc /= 0.95
        return learned, back_level

    # Root-level units.
    for lit in unit_literals:
        if not enqueue(lit, -1):
            print("NO")
            return

    conflict = propagate()
    if conflict != -1:
        print("NO")
        return

    conflicts_since_restart = 0
    restart_limit = 100

    while True:
        conflict = propagate()

        if conflict != -1:
            if len(trail_lim) == 0:
                print("NO")
                return

            learned, back_level = analyze(conflict)
            backtrack(back_level)

            cid = len(clauses)
            clauses.append(learned)

            if len(learned) >= 2:
                watches[widx(learned[0])].append(cid)
                watches[widx(learned[1])].append(cid)

            if not enqueue(learned[0], cid):
                print("NO")
                return

            conflicts_since_restart += 1
            if conflicts_since_restart >= restart_limit:
                backtrack(0)
                conflicts_since_restart = 0
                restart_limit = int(restart_limit * 1.5) + 1
            continue

        decision_var = 0
        while heap:
            _, v = heapq.heappop(heap)
            if assignment[v] == -1:
                decision_var = v
                break

        if decision_var == 0:
            break

        trail_lim.append(len(trail))
        # Prefer false; exact-one clauses will force the remaining color.
        enqueue(-decision_var, -1)

    for eid in range(m):
        chosen = -1
        for color in range(3):
            if assignment[3 * eid + color + 1] == 1:
                chosen = color
                break
        if chosen == -1:
            print("NO")
            return
        answer[eid] = chosen

    print("YES")
    print(*[x + 1 for x in answer])


if __name__ == "__main__":
    main()