import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    B = int(data[idx]); idx += 1

    anchors = []
    for _ in range(k):
        anchors.append(int(data[idx]) - 1)
        idx += 1

    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        w = int(data[idx]); idx += 1
        edges.append((u, v, w))

    # Sort edges by weight ascending
    edges.sort(key=lambda x: x[2])

    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True

    total = 0
    chosen = []

    for u, v, w in edges:
        ru = find(u)
        rv = find(v)
        if ru == rv:
            continue
        # Check if both components contain at least one anchor
        # We track this by checking if any anchor is in ru and any in rv
        # Since anchors are few, we can check by seeing if find(anchor) == ru or rv
        # But to be efficient, we can precompute anchor roots
        # However, simpler: check if any anchor's root is ru and any anchor's root is rv
        # Since k can be up to n, but typically small, we do a quick check
        # Actually, we can maintain a set of roots that contain anchors
        # But for simplicity, we check on the fly
        # If both components have anchors, we must cut this edge
        # Otherwise, we can safely merge
        # To check: see if there exists an anchor a with find(a) == ru and an anchor b with find(b) == rv
        # Since k might be large, we can maintain a boolean array or set
        # Let's maintain a set of roots that contain anchors
        # But we need to update on union
        # For now, since k is not specified to be small, we use a set
        # But to avoid O(k) per edge, we can maintain a dict root -> count of anchors
        pass

    # Redo with anchor count tracking
    parent = list(range(n))
    rank = [0] * n
    anchor_count = [0] * n
    for a in anchors:
        anchor_count[a] += 1

    def find2(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    total = 0
    chosen = []

    for u, v, w in edges:
        ru = find2(u)
        rv = find2(v)
        if ru == rv:
            continue
        if anchor_count[ru] > 0 and anchor_count[rv] > 0:
            # Must cut this edge
            if total + w > B:
                print("NO")
                return
            total += w
            chosen.append((u, v))
        else:
            # Merge
            if rank[ru] < rank[rv]:
                parent[ru] = rv
                anchor_count[rv] += anchor_count[ru]
            elif rank[ru] > rank[rv]:
                parent[rv] = ru
                anchor_count[ru] += anchor_count[rv]
            else:
                parent[rv] = ru
                anchor_count[ru] += anchor_count[rv]
                rank[ru] += 1

    print("YES")
    print(len(chosen))
    for u, v in chosen:
        print(u + 1, v + 1)

solve()