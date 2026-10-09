import sys

sys.setrecursionlimit(1000000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    raise SystemExit

n, m = data[0], data[1]
adj = [0] * n

p = 2
for _ in range(m):
    u = data[p] - 1
    v = data[p + 1] - 1
    p += 2
    if u != v:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

FULL = (1 << n) - 1
failed = set()


def is_bipartite(mask):
    color = [-1] * n
    unseen = mask

    while unseen:
        bit = unseen & -unseen
        root = bit.bit_length() - 1
        unseen ^= bit
        color[root] = 0
        queue = [root]
        head = 0

        while head < len(queue):
            u = queue[head]
            head += 1
            neighbors = adj[u] & mask
            while neighbors:
                bit = neighbors & -neighbors
                neighbors ^= bit
                v = bit.bit_length() - 1

                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    unseen &= ~bit
                    queue.append(v)
                elif color[v] == color[u]:
                    return False

    return True


def make_cycle(u, v, parent):
    ancestors = 0
    x = u
    while x != -1:
        ancestors |= 1 << x
        x = parent[x]

    y = v
    while not ((ancestors >> y) & 1):
        y = parent[y]
    lca = y

    cycle = 1 << lca
    x = u
    while x != lca:
        cycle |= 1 << x
        x = parent[x]

    y = v
    while y != lca:
        cycle |= 1 << y
        y = parent[y]

    return cycle


def analyze(mask, forbidden):
    best_cycle = 0
    best_count = n + 1

    # Triangles provide especially strong branching cycles.
    vertices = mask
    while vertices:
        ub = vertices & -vertices
        vertices ^= ub
        u = ub.bit_length() - 1

        vs = adj[u] & mask & ~((1 << (u + 1)) - 1)
        while vs:
            vb = vs & -vs
            vs ^= vb
            v = vb.bit_length() - 1

            common = adj[u] & adj[v] & mask & ~((1 << (v + 1)) - 1)
            while common:
                wb = common & -common
                common ^= wb
                cycle = ub | vb | wb
                count = (cycle & ~forbidden).bit_count()
                if count < best_count:
                    best_count = count
                    best_cycle = cycle
                    if count <= 1:
                        return None, best_cycle

    color = [-1] * n
    parent = [-1] * n
    unseen = mask
    part0 = 0
    part1 = 0
    has_conflict = False

    while unseen:
        bit = unseen & -unseen
        root = bit.bit_length() - 1
        unseen ^= bit
        color[root] = 0
        part0 |= bit
        queue = [root]
        head = 0

        while head < len(queue):
            u = queue[head]
            head += 1
            neighbors = adj[u] & mask

            while neighbors:
                bit = neighbors & -neighbors
                neighbors ^= bit
                v = bit.bit_length() - 1

                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    parent[v] = u
                    unseen &= ~bit
                    if color[v] == 0:
                        part0 |= bit
                    else:
                        part1 |= bit
                    queue.append(v)
                elif color[v] == color[u] and u < v:
                    has_conflict = True
                    cycle = make_cycle(u, v, parent)
                    count = (cycle & ~forbidden).bit_count()
                    if count < best_count:
                        best_count = count
                        best_cycle = cycle
                        if count <= 1:
                            return None, best_cycle

    if not has_conflict:
        return (part0, part1), 0
    return None, best_cycle


def solve(mask, forbidden):
    if mask in failed:
        return None

    # Forbidden vertices can never be assigned color 1. If they already
    # contain an odd cycle, no completion is possible.
    if not is_bipartite(mask & forbidden):
        failed.add(mask)
        return None

    partition, cycle = analyze(mask, forbidden)
    if partition is not None:
        return mask, partition[0], partition[1]

    candidates = cycle & mask & ~forbidden
    if not candidates:
        failed.add(mask)
        return None

    order = []
    while candidates:
        bit = candidates & -candidates
        candidates ^= bit
        v = bit.bit_length() - 1
        order.append(((adj[v] & mask).bit_count(), v))

    order.sort(reverse=True)

    for _, v in order:
        bit = 1 << v
        result = solve(mask ^ bit, forbidden | adj[v])
        if result is not None:
            return result

    failed.add(mask)
    return None


result = solve(FULL, 0)

if result is None:
    print("NO")
else:
    remaining, part0, part1 = result
    selected = FULL ^ remaining
    answer = [0] * n

    for i in range(n):
        bit = 1 << i
        if selected & bit:
            answer[i] = 1
        elif part0 & bit:
            answer[i] = 2
        else:
            answer[i] = 3

    print("YES")
    print(*answer)