import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    NT = int(next(it))
    NR = int(next(it))
    M = int(next(it))

    # adjacency list for transmitters: list of (edge_id, receiver)
    adj = [[] for _ in range(NT + 1)]
    deg_left = [0] * (NT + 1)
    deg_right = [0] * (NR + 1)

    edges = []                     # store (u, v) for possible later use
    for eid in range(M):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((eid, v))
        deg_left[u] += 1
        deg_right[v] += 1

    K = 0
    for d in deg_left:
        if d > K:
            K = d
    for d in deg_right:
        if d > K:
            K = d

    answer = [0] * M

    # active transmitters (still have uncoloured edges)
    active = [u for u in range(1, NT + 1) if deg_left[u] > 0]
    ptr = [0] * (NT + 1)           # pointer inside adj[u]

    # timestamp array for receivers
    used_round = [0] * (NR + 1)

    for colour in range(1, K + 1):
        next_active = []
        for u in active:
            # skip already coloured edges
            lst = adj[u]
            p = ptr[u]
            while p < len(lst) and answer[lst[p][0]] != 0:
                p += 1
            ptr[u] = p
            if p == len(lst):
                continue          # no edges left for this transmitter
            eid, v = lst[p]
            if used_round[v] != colour:   # receiver free this round
                answer[eid] = colour
                used_round[v] = colour
                ptr[u] = p + 1            # this edge is now coloured
            # keep u for next round if it still has edges
            if ptr[u] < len(lst):
                next_active.append(u)
        active = next_active

    # all edges must be coloured now
    out = ['YES\n', ' '.join(str(c) for c in answer)]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()