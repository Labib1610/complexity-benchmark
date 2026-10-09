import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    Nα = int(next(it))
    Nω = int(next(it))
    m = int(next(it))

    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    degA = [0] * Nα
    degB = [0] * Nω
    for u, v in edges:
        degA[u] += 1
        degB[v] += 1
    K = max(max(degA) if Nα else 0, max(degB) if Nω else 0)

    # adjacency for alternating path search
    adjA = [[] for _ in range(Nα)]
    adjB = [[] for _ in range(Nω)]
    for idx, (u, v) in enumerate(edges):
        adjA[u].append((v, idx))
        adjB[v].append((u, idx))

    usedA = [set() for _ in range(Nα)]
    usedB = [set() for _ in range(Nω)]
    ptrA = [1] * Nα
    ptrB = [1] * Nω

    colour = [0] * m

    from collections import deque

    for idx, (u, v) in enumerate(edges):
        # try greedy colour
        while ptrA[u] in usedA[u]:
            ptrA[u] += 1
        while ptrB[v] in usedB[v]:
            ptrB[v] += 1
        c = max(ptrA[u], ptrB[v])
        while c <= K and (c in usedA[u] or c in usedB[v]):
            c += 1
        if c <= K:
            colour[idx] = c
            usedA[u].add(c)
            usedB[v].add(c)
            continue

        # need alternating path
        # a free at u, b free at v
        a = ptrA[u]          # guaranteed free at u
        b = ptrB[v]          # guaranteed free at v

        # BFS to find vertex where b is free, starting from u following a/b alternation
        # we keep predecessor edge to reconstruct path
        prev = dict()        # key: (side, vertex) -> (prev_side, prev_vertex, edge_idx)
        q = deque()
        q.append(('A', u))
        prev[('A', u)] = None

        target = None
        while q:
            side, x = q.popleft()
            if side == 'A':
                # we arrived via colour b, now look for a‑edge
                for nb, eidx in adjA[x]:
                    if colour[eidx] != a:
                        continue
                    nxt = ('B', nb)
                    if nxt not in prev:
                        prev[nxt] = ('A', x, eidx)
                        q.append(nxt)
            else:  # side == 'B'
                # we arrived via colour a, now look for b‑edge
                for nb, eidx in adjB[x]:
                    if colour[eidx] != b:
                        continue
                    nxt = ('A', nb)
                    if nxt not in prev:
                        prev[nxt] = ('B', x, eidx)
                        q.append(nxt)

            # check if current vertex has free colour b (only for side B)
            if side == 'B' and b not in usedB[x]:
                target = ('B', x)
                break

        # reconstruct path and swap colours a <-> b
        cur = target
        while cur != ('A', u):
            p = prev[cur]
            if p is None:
                break
            prev_side, prev_vert, eidx = p
            # swap colour on edge eidx
            if colour[eidx] == a:
                colour[eidx] = b
                usedA[edges[eidx][0]].remove(a)
                usedA[edges[eidx][0]].add(b)
                usedB[edges[eidx][1]].remove(a)
                usedB[edges[eidx][1]].add(b)
            else:
                colour[eidx] = a
                usedA[edges[eidx][0]].remove(b)
                usedA[edges[eidx][0]].add(a)
                usedB[edges[eidx][1]].remove(b)
                usedB[edges[eidx][1]].add(a)
            cur = (prev_side, prev_vert)

        # now colour the original edge with a
        colour[idx] = a
        usedA[u].add(a)
        usedB[v].add(a)

    out = ['YES', ' '.join(str(c) for c in colour)]
    sys.stdout.write('\n'.join(out))

if __name__ == '__main__':
    solve()