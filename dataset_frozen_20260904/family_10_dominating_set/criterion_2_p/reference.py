import sys
from collections import deque


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); idx += 2
        adj[u].append(v); adj[v].append(u)

    INF = n + 5
    # Root the tree at 1, build parent/children and a post-order via BFS.
    parent = [0] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    visited[1] = True
    q = deque([1])
    while q:
        u = q.popleft(); order.append(u)
        for w in adj[u]:
            if not visited[w]:
                visited[w] = True; parent[w] = u; q.append(w)
    children = [[] for _ in range(n + 1)]
    for v in order[1:]:
        children[parent[v]].append(v)

    # 3-state tree DP for minimum dominating set.
    #   IN  : v is in the set
    #   DOM : v not in set, dominated by a child in the set
    #   UND : v not in set, not dominated by any child (needs its parent in the set)
    IN = [0] * (n + 1); DOM = [0] * (n + 1); UND = [0] * (n + 1)
    for v in reversed(order):
        ch = children[v]
        s_in = 1
        s_und = 0
        base = 0                      # sum of min(IN_c, DOM_c) over children
        best_delta = INF              # cheapest cost to force one child IN (for DOM)
        has_in = False
        for c in ch:
            s_in += min(IN[c], DOM[c], UND[c])
            s_und += DOM[c]
            mc = IN[c] if IN[c] <= DOM[c] else DOM[c]
            base += mc
            if IN[c] <= DOM[c]:
                has_in = True
            else:
                d = IN[c] - DOM[c]
                if d < best_delta:
                    best_delta = d
        IN[v] = s_in
        UND[v] = s_und
        if not ch:
            DOM[v] = INF              # a leaf cannot be dominated by a child
        elif has_in:
            DOM[v] = base
        else:
            DOM[v] = base + best_delta

    root_state = "IN" if IN[1] <= DOM[1] else "DOM"
    best = min(IN[1], DOM[1])

    if best > k:
        sys.stdout.write("NO\n")
        return

    # Reconstruct one optimal dominating set by walking the states top-down.
    in_set = []
    st = [(1, root_state)]
    while st:
        v, state = st.pop()
        ch = children[v]
        if state == "IN":
            in_set.append(v)
            for c in ch:
                mn = min(IN[c], DOM[c], UND[c])
                cs = "IN" if IN[c] == mn else ("DOM" if DOM[c] == mn else "UND")
                st.append((c, cs))
        elif state == "UND":
            for c in ch:
                st.append((c, "DOM"))
        else:  # DOM: children IN or DOM, at least one IN
            picks = []
            has_in = False
            for c in ch:
                if IN[c] <= DOM[c]:
                    picks.append((c, "IN")); has_in = True
                else:
                    picks.append((c, "DOM"))
            if not has_in and ch:
                # force the cheapest child to IN
                bi = min(range(len(ch)), key=lambda i: IN[ch[i]] - DOM[ch[i]])
                picks[bi] = (ch[bi], "IN")
            st.extend(picks)

    in_set.sort()
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, in_set)) + "\n")


main()
