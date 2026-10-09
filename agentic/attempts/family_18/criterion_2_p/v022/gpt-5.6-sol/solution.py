import sys
from array import array
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, B = data[0], data[1], data[2]
    adj_list = [[] for _ in range(n)]
    adj_mask = [0] * n

    edges = []
    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        edges.append((u, v))
        adj_list[u].append(v)
        adj_list[v].append(u)
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    if B < m:
        print("NO")
        return

    def positions(order):
        pos = [0] * n
        for i, v in enumerate(order, 1):
            pos[v] = i
        return pos

    def arrangement_cost(order):
        pos = [0] * n
        for i, v in enumerate(order):
            pos[v] = i
        return sum(abs(pos[u] - pos[v]) for u, v in edges)

    def improve(order):
        order = order[:]
        pos = [0] * n
        for i, v in enumerate(order):
            pos[v] = i

        for _ in range(min(3 * n + 1, 10000)):
            changed = False
            for i in range(n - 1):
                x, y = order[i], order[i + 1]
                delta = 0

                for z in adj_list[x]:
                    if z != y:
                        delta += abs(i + 1 - pos[z]) - abs(i - pos[z])
                for z in adj_list[y]:
                    if z != x:
                        delta += abs(i - pos[z]) - abs(i + 1 - pos[z])

                if delta < 0:
                    order[i], order[i + 1] = y, x
                    pos[x], pos[y] = i + 1, i
                    changed = True
            if not changed:
                break
        return order

    candidates = [list(range(n))]

    if n:
        roots = {0, n - 1}
        roots.add(max(range(n), key=lambda x: len(adj_list[x])))
        leaves = [i for i in range(n) if len(adj_list[i]) <= 1]
        if leaves:
            roots.add(leaves[0])
            roots.add(leaves[-1])

        for root in roots:
            order = []
            stack = [(root, -1)]
            while stack:
                v, parent = stack.pop()
                order.append(v)
                children = [x for x in adj_list[v] if x != parent]
                children.sort(key=lambda x: len(adj_list[x]), reverse=True)
                for x in reversed(children):
                    stack.append((x, v))
            candidates.append(order)

            q = deque([root])
            parent = [-2] * n
            parent[root] = -1
            bfs = []
            while q:
                v = q.popleft()
                bfs.append(v)
                children = [x for x in adj_list[v] if parent[x] == -2]
                children.sort(key=lambda x: len(adj_list[x]))
                for x in children:
                    parent[x] = v
                    q.append(x)
            candidates.append(bfs)
            candidates.append(bfs[::-1])

    best_order = None
    best_cost = None
    for order in candidates:
        for candidate in (order, improve(order)):
            cost = arrangement_cost(candidate)
            if best_cost is None or cost < best_cost:
                best_cost = cost
                best_order = candidate[:]
            if cost <= B:
                print("YES")
                print(*positions(candidate))
                return

    if n <= 22:
        size = 1 << n
        full = size - 1
        inf = B + 1

        cuts = array('i', [0]) * size
        dp = array('q', [inf]) * size
        dp[0] = 0
        degrees = [len(x) for x in adj_list]

        cuts_local = cuts
        dp_local = dp
        masks_local = adj_mask
        deg_local = degrees

        for mask in range(1, size):
            bit = mask & -mask
            v = bit.bit_length() - 1
            prev = mask ^ bit
            c = cuts_local[prev] + deg_local[v] - 2 * ((masks_local[v] & prev).bit_count())
            cuts_local[mask] = c

            bits = mask
            best = inf
            while bits:
                b = bits & -bits
                value = dp_local[mask ^ b]
                if value < best:
                    best = value
                bits ^= b

            value = best + c
            if value <= B:
                dp_local[mask] = value

        if dp_local[full] > B:
            print("NO")
            return

        order_rev = []
        mask = full
        while mask:
            current = dp_local[mask]
            c = cuts_local[mask]
            bits = mask
            found = False
            while bits:
                bit = bits & -bits
                prev = mask ^ bit
                if dp_local[prev] + c == current:
                    order_rev.append(bit.bit_length() - 1)
                    mask = prev
                    found = True
                    break
                bits ^= bit
            if not found:
                print("NO")
                return

        order_rev.reverse()
        print("YES")
        print(*positions(order_rev))
        return

    base = n + 1
    full = (1 << n) - 1
    layers = [{0: 0}]

    for _ in range(n):
        current_layer = layers[-1]
        next_layer = {}

        for mask, encoded in current_layer.items():
            cost, cut = divmod(encoded, base)
            remaining = full ^ mask

            while remaining:
                bit = remaining & -remaining
                v = bit.bit_length() - 1
                new_mask = mask | bit
                new_cut = cut + len(adj_list[v]) - 2 * ((adj_mask[v] & mask).bit_count())
                new_cost = cost + new_cut

                if new_cost <= B:
                    new_encoded = new_cost * base + new_cut
                    old = next_layer.get(new_mask)
                    if old is None or new_encoded < old:
                        next_layer[new_mask] = new_encoded

                remaining ^= bit

        if not next_layer:
            print("NO")
            return
        layers.append(next_layer)

    if full not in layers[n]:
        print("NO")
        return

    order_rev = []
    mask = full
    for k in range(n, 0, -1):
        encoded = layers[k][mask]
        cost, cut = divmod(encoded, base)
        bits = mask
        found = False

        while bits:
            bit = bits & -bits
            prev = mask ^ bit
            prev_encoded = layers[k - 1].get(prev)
            if prev_encoded is not None:
                prev_cost = prev_encoded // base
                if prev_cost + cut == cost:
                    order_rev.append(bit.bit_length() - 1)
                    mask = prev
                    found = True
                    break
            bits ^= bit

        if not found:
            print("NO")
            return

    order_rev.reverse()
    print("YES")
    print(*positions(order_rev))

if __name__ == "__main__":
    main()