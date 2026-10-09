import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, k = data[0], data[1], data[2]

    if k == 1:
        print("YES")
        print(1)
        return

    conflicts = [0] * n
    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        conflicts[u] |= 1 << v
        conflicts[v] |= 1 << u

    full = (1 << n) - 1
    adj = [0] * n
    for v in range(n):
        adj[v] = full & ~(conflicts[v] | (1 << v))

    # A vertex in a k-clique must belong to the (k-1)-core.
    active = full
    degree = [adj[v].bit_count() for v in range(n)]
    queue = deque(v for v in range(n) if degree[v] < k - 1)

    while queue:
        v = queue.popleft()
        bv = 1 << v
        if not (active & bv):
            continue
        active ^= bv
        neighbors = adj[v] & active
        while neighbors:
            b = neighbors & -neighbors
            neighbors ^= b
            u = b.bit_length() - 1
            degree[u] -= 1
            if degree[u] == k - 2:
                queue.append(u)

    if active.bit_count() < k:
        print("NO")
        return

    # Fast greedy attempts.
    starts = []
    bits = active
    while bits:
        b = bits & -bits
        bits ^= b
        starts.append(b.bit_length() - 1)
    starts.sort(key=lambda v: degree[v], reverse=True)

    for start in starts:
        clique = [start]
        candidates = active & adj[start]
        while len(clique) < k and candidates:
            q = candidates
            best = -1
            best_degree = -1
            while q:
                b = q & -q
                q ^= b
                v = b.bit_length() - 1
                d = (adj[v] & candidates).bit_count()
                if d > best_degree:
                    best_degree = d
                    best = v
            clique.append(best)
            candidates &= adj[best]
        if len(clique) == k:
            print("YES")
            print(" ".join(str(v + 1) for v in clique))
            return

    # Cliques cannot span connected components of the compatibility graph.
    components = []
    unseen = active
    while unseen:
        seed = unseen & -unseen
        stack = seed
        component = 0
        unseen ^= seed

        while stack:
            b = stack & -stack
            stack ^= b
            v = b.bit_length() - 1
            component |= b

            new_vertices = adj[v] & unseen
            unseen &= ~new_vertices
            stack |= new_vertices

        if component.bit_count() >= k:
            components.append(component)

    components.sort(key=int.bit_count, reverse=True)
    sys.setrecursionlimit(1000)

    def search_component(component):
        old_vertices = []
        q = component
        while q:
            b = q & -q
            q ^= b
            old_vertices.append(b.bit_length() - 1)

        old_vertices.sort(
            key=lambda v: (adj[v] & component).bit_count()
        )

        size = len(old_vertices)
        position = [-1] * n
        for i, v in enumerate(old_vertices):
            position[v] = i

        local_adj = [0] * size
        for i, v in enumerate(old_vertices):
            neighbors = adj[v] & component
            mask = 0
            while neighbors:
                b = neighbors & -neighbors
                neighbors ^= b
                u = b.bit_length() - 1
                mask |= 1 << position[u]
            local_adj[i] = mask

        chosen = []
        answer = None
        bit_count = int.bit_count

        def expand(candidates, depth):
            nonlocal answer

            count = bit_count(candidates)
            need = k - depth
            if count < need:
                return False

            if need == 1:
                b = candidates & -candidates
                answer = chosen + [b.bit_length() - 1]
                return True

            if need == 2:
                q2 = candidates
                while q2:
                    b = q2 & -q2
                    q2 ^= b
                    v = b.bit_length() - 1
                    common = candidates & local_adj[v]
                    if common:
                        u = (common & -common).bit_length() - 1
                        answer = chosen + [v, u]
                        return True
                return False

            order = []
            colors = []
            remaining = candidates
            color = 0

            while remaining:
                color += 1
                available = remaining
                while available:
                    b = available & -available
                    available ^= b
                    remaining ^= b
                    v = b.bit_length() - 1
                    order.append(v)
                    colors.append(color)
                    available &= ~local_adj[v]

            for i in range(len(order) - 1, -1, -1):
                if depth + colors[i] < k:
                    return False

                v = order[i]
                bv = 1 << v
                chosen.append(v)

                next_candidates = candidates & local_adj[v]
                if expand(next_candidates, depth + 1):
                    return True

                chosen.pop()
                candidates ^= bv

            return False

        if expand((1 << size) - 1, 0):
            return [old_vertices[v] for v in answer]
        return None

    for component in components:
        result = search_component(component)
        if result is not None:
            print("YES")
            print(" ".join(str(v + 1) for v in result))
            return

    print("NO")

if __name__ == "__main__":
    main()