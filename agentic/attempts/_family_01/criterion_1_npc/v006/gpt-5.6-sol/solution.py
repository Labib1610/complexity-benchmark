import sys

sys.setrecursionlimit(100000)


def bipartite_coloring(adj):
    n = len(adj)
    color = [-1] * n
    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        stack = [start]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    stack.append(v)
                elif color[v] == color[u]:
                    return None
    return color


def solve_component(adj):
    n = len(adj)

    easy = bipartite_coloring(adj)
    if easy is not None:
        return easy

    masks = [0] * n
    degrees = [len(x) for x in adj]
    for u in range(n):
        mask = 0
        for v in adj[u]:
            mask |= 1 << v
        masks[u] = mask

    triangle = None
    best_score = -1
    for u in range(n):
        for v in adj[u]:
            if v <= u:
                continue
            common = masks[u] & masks[v]
            while common:
                bit = common & -common
                w = bit.bit_length() - 1
                common -= bit
                if w > v:
                    score = degrees[u] + degrees[v] + degrees[w]
                    if score > best_score:
                        best_score = score
                        triangle = (u, v, w)

    domains = [7] * n
    trail = []

    def assign_and_propagate(seeds):
        queue = []
        for v, value in seeds:
            old = domains[v]
            if not (old & value):
                return False
            if old != value:
                trail.append((v, old))
                domains[v] = value
                queue.append(v)

        pos = 0
        while pos < len(queue):
            u = queue[pos]
            pos += 1
            value = domains[u]

            for v in adj[u]:
                old = domains[v]
                if not (old & value):
                    continue

                new = old & ~value
                trail.append((v, old))
                domains[v] = new

                if new == 0:
                    return False
                if new & (new - 1) == 0 and old & (old - 1) != 0:
                    queue.append(v)

        return True

    if triangle is not None:
        a, b, c = triangle
        initial = [(a, 1), (b, 2), (c, 4)]
    else:
        best_edge = None
        best_score = -1
        for u in range(n):
            for v in adj[u]:
                if u < v:
                    score = degrees[u] + degrees[v]
                    if score > best_score:
                        best_score = score
                        best_edge = (u, v)
        a, b = best_edge
        initial = [(a, 1), (b, 2)]

    if not assign_and_propagate(initial):
        return None
    trail.clear()

    def solve_two_domains():
        variables = []
        index = [-1] * n
        options = []

        for v in range(n):
            d = domains[v]
            if d & (d - 1):
                index[v] = len(variables)
                variables.append(v)
                bits = []
                x = d
                while x:
                    bit = x & -x
                    bits.append(bit)
                    x -= bit
                if len(bits) != 2:
                    return None
                options.append(bits)

        k = len(variables)
        if k == 0:
            return [domains[v].bit_length() - 1 for v in range(n)]

        graph = [[] for _ in range(2 * k)]
        reverse = [[] for _ in range(2 * k)]

        def add_implication(a, b):
            graph[a].append(b)
            reverse[b].append(a)

        for u in range(n):
            for v in adj[u]:
                if v <= u:
                    continue

                iu = index[u]
                iv = index[v]

                if iu == -1 and iv == -1:
                    if domains[u] == domains[v]:
                        return None
                    continue

                if iu == -1 or iv == -1:
                    # Such conflicts should already have been propagated.
                    fixed = domains[u] if iu == -1 else domains[v]
                    var_idx = iv if iu == -1 else iu
                    opts = options[var_idx]
                    for choice in range(2):
                        if opts[choice] == fixed:
                            node = 2 * var_idx + choice
                            add_implication(node, node ^ 1)
                    continue

                common = domains[u] & domains[v]
                while common:
                    color_bit = common & -common
                    common -= color_bit
                    cu = 0 if options[iu][0] == color_bit else 1
                    cv = 0 if options[iv][0] == color_bit else 1
                    lu = 2 * iu + cu
                    lv = 2 * iv + cv
                    add_implication(lu, lv ^ 1)
                    add_implication(lv, lu ^ 1)

        visited = [False] * (2 * k)
        order = []

        def dfs1(start):
            stack = [(start, 0)]
            visited[start] = True
            while stack:
                u, pos = stack[-1]
                if pos < len(graph[u]):
                    v = graph[u][pos]
                    stack[-1] = (u, pos + 1)
                    if not visited[v]:
                        visited[v] = True
                        stack.append((v, 0))
                else:
                    order.append(u)
                    stack.pop()

        for node in range(2 * k):
            if not visited[node]:
                dfs1(node)

        component = [-1] * (2 * k)
        component_id = 0

        for start in reversed(order):
            if component[start] != -1:
                continue
            component[start] = component_id
            stack = [start]
            while stack:
                u = stack.pop()
                for v in reverse[u]:
                    if component[v] == -1:
                        component[v] = component_id
                        stack.append(v)
            component_id += 1

        result = [-1] * n
        for v in range(n):
            if index[v] == -1:
                result[v] = domains[v].bit_length() - 1

        for i, v in enumerate(variables):
            if component[2 * i] == component[2 * i + 1]:
                return None
            choice = 0 if component[2 * i] > component[2 * i + 1] else 1
            result[v] = options[i][choice].bit_length() - 1

        return result

    def search():
        has_three = False
        candidate = -1
        candidate_score = None

        for v in range(n):
            d = domains[v]
            count = d.bit_count()
            if count == 3:
                has_three = True
            elif count == 2:
                neighbors_three = 0
                neighbors_unfixed = 0
                for w in adj[v]:
                    bc = domains[w].bit_count()
                    if bc == 3:
                        neighbors_three += 1
                    if bc > 1:
                        neighbors_unfixed += 1
                score = (neighbors_three, neighbors_unfixed, degrees[v])
                if candidate_score is None or score > candidate_score:
                    candidate_score = score
                    candidate = v

        if not has_three:
            return solve_two_domains()

        if candidate == -1:
            for v in range(n):
                if domains[v].bit_count() == 3:
                    candidate = v
                    break

        available = []
        x = domains[candidate]
        while x:
            bit = x & -x
            x -= bit
            impact = sum(1 for w in adj[candidate] if domains[w] & bit)
            available.append((impact, bit))
        available.sort(reverse=True)

        for _, value in available:
            mark = len(trail)
            if assign_and_propagate([(candidate, value)]):
                answer = search()
                if answer is not None:
                    return answer
            while len(trail) > mark:
                v, old = trail.pop()
                domains[v] = old

        return None

    return search()


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    global_adj = [set() for _ in range(n)]
    p = 2

    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u == v:
            print("NO")
            return
        global_adj[u].add(v)
        global_adj[v].add(u)

    answer = [-1] * n
    seen = [False] * n

    for start in range(n):
        if seen[start]:
            continue

        seen[start] = True
        stack = [start]
        vertices = []

        while stack:
            u = stack.pop()
            vertices.append(u)
            for v in global_adj[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)

        position = {v: i for i, v in enumerate(vertices)}
        local_adj = [[] for _ in vertices]

        for i, u in enumerate(vertices):
            local_adj[i] = [position[v] for v in global_adj[u]]

        local_answer = solve_component(local_adj)
        if local_answer is None:
            print("NO")
            return

        for i, v in enumerate(vertices):
            answer[v] = local_answer[i] + 1

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()