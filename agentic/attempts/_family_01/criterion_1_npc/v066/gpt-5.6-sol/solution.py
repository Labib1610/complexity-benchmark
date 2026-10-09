import sys

sys.setrecursionlimit(10000)

def solve_component(vertices, adj, degree):
    n = len(adj)
    vertex_set = set(vertices)

    # Prefer fixing all three colors on a triangle to eliminate color symmetry.
    best_triangle = None
    best_score = -1
    for i in vertices:
        neighbors = [v for v in adj[i] if v in vertex_set and v > i]
        for x in range(len(neighbors)):
            a = neighbors[x]
            for y in range(x + 1, len(neighbors)):
                b = neighbors[y]
                if b in adj[a]:
                    score = degree[i] + degree[a] + degree[b]
                    if score > best_score:
                        best_score = score
                        best_triangle = (i, a, b)

    if best_triangle is not None:
        seeds = [
            (best_triangle[0], 0),
            (best_triangle[1], 1),
            (best_triangle[2], 2),
        ]
    else:
        root = max(vertices, key=lambda v: degree[v])
        neighbor = max(adj[root], key=lambda v: degree[v])
        seeds = [(root, 0), (neighbor, 1)]

    colors = [-1] * n
    domains = [7] * n

    def propagate(cur_colors, cur_domains, initial):
        queue = list(initial)
        head = 0

        while head < len(queue):
            v, c = queue[head]
            head += 1
            bit = 1 << c

            if cur_colors[v] != -1:
                if cur_colors[v] != c:
                    return False
                continue

            if not (cur_domains[v] & bit):
                return False

            cur_colors[v] = c
            cur_domains[v] = bit

            for u in adj[v]:
                if cur_colors[u] != -1:
                    if cur_colors[u] == c:
                        return False
                elif cur_domains[u] & bit:
                    new_domain = cur_domains[u] & ~bit
                    if new_domain == 0:
                        return False
                    cur_domains[u] = new_domain
                    if new_domain & (new_domain - 1) == 0:
                        queue.append((u, new_domain.bit_length() - 1))

        return True

    if not propagate(colors, domains, seeds):
        return None

    def dfs(cur_colors, cur_domains):
        chosen = -1
        best_key = None

        for v in vertices:
            if cur_colors[v] == -1:
                size = cur_domains[v].bit_count()
                uncolored_degree = sum(
                    1 for u in adj[v] if cur_colors[u] == -1
                )
                key = (size, -uncolored_degree, -degree[v])
                if best_key is None or key < best_key:
                    best_key = key
                    chosen = v

        if chosen == -1:
            return cur_colors

        candidates = []
        mask = cur_domains[chosen]
        for c in range(3):
            bit = 1 << c
            if mask & bit:
                impact = sum(
                    1
                    for u in adj[chosen]
                    if cur_colors[u] == -1 and (cur_domains[u] & bit)
                )
                candidates.append((impact, c))

        candidates.sort()

        for _, c in candidates:
            next_colors = cur_colors.copy()
            next_domains = cur_domains.copy()
            if propagate(next_colors, next_domains, [(chosen, c)]):
                result = dfs(next_colors, next_domains)
                if result is not None:
                    return result

        return None

    return dfs(colors, domains)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj = [set() for _ in range(n)]
    impossible = False

    pos = 2
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        if u == v:
            impossible = True
        else:
            adj[u].add(v)
            adj[v].add(u)

    if impossible:
        print("NO")
        return

    degree = [len(adj[v]) for v in range(n)]
    visited = [False] * n
    answer = [-1] * n

    for start in range(n):
        if visited[start]:
            continue

        stack = [start]
        visited[start] = True
        component = []

        while stack:
            v = stack.pop()
            component.append(v)
            for u in adj[v]:
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)

        # Bipartite components need only two colors.
        bip_color = {component[0]: 0}
        queue = [component[0]]
        head = 0
        bipartite = True

        while head < len(queue) and bipartite:
            v = queue[head]
            head += 1
            for u in adj[v]:
                if u not in bip_color:
                    bip_color[u] = bip_color[v] ^ 1
                    queue.append(u)
                elif bip_color[u] == bip_color[v]:
                    bipartite = False
                    break

        if bipartite:
            for v in component:
                answer[v] = bip_color[v]
            continue

        result = solve_component(component, adj, degree)
        if result is None:
            print("NO")
            return

        for v in component:
            answer[v] = result[v]

    print("YES")
    print(*[c + 1 for c in answer])


if __name__ == "__main__":
    main()