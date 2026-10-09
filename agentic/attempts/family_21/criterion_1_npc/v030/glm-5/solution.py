import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
    anchors = [int(next(it)) for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))

    if k <= 1:
        print("YES")
        print(0)
        return

    parent = list(range(n + 1))

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        parent[rx] = ry
        return True

    edges.sort(key=lambda e: e[2])

    total = 0
    cut_edges = []
    for u, v, w in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            continue
        # Check if merging would connect two anchors.
        # We track anchor presence via parent root.
        # Since anchors are never merged, ru is anchor-root iff ru is an anchor.
        if ru in anchor_set and rv in anchor_set:
            cut_edges.append((u, v, w))
            total += w
            if total > B:
                print("NO")
                return
        else:
            parent[ru] = rv

    print("YES")
    print(len(cut_edges))
    out = []
    for u, v, _ in cut_edges:
        out.append(f"{u} {v}")
    sys.stdout.write("\n".join(out))
    if out:
        sys.stdout.write("\n")

anchor_set = set()
# We need anchor_set before solve uses it; restructure:
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
    anchors = [int(next(it)) for _ in range(k)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))

    if k <= 1:
        print("YES")
        print(0)
        return

    anchor_set = set(anchors)
    parent = list(range(n + 1))

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    edges.sort(key=lambda e: e[2])

    total = 0
    cut_edges = []
    for u, v, w in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            continue
        if ru in anchor_set and rv in anchor_set:
            cut_edges.append((u, v, w))
            total += w
            if total > B:
                print("NO")
                return
        else:
            parent[ru] = rv

    print("YES")
    print(len(cut_edges))
    out = []
    for u, v, _ in cut_edges:
        out.append(f"{u} {v}")
    sys.stdout.write("\n".join(out))
    if out:
        sys.stdout.write("\n")

main()