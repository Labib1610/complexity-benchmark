import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    nL = int(next(it))
    nR = int(next(it))
    m = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    degL = [0] * nL
    degR = [0] * nR
    for u, v in edges:
        degL[u] += 1
        degR[v] += 1
    Delta = max(max(degL) if nL else 0, max(degR) if nR else 0)

    usedL = [set() for _ in range(nL)]
    usedR = [set() for _ in range(nR)]
    ptrL = [1] * nL
    ptrR = [1] * nR

    ans = [0] * m
    for idx, (u, v) in enumerate(edges):
        c = max(ptrL[u], ptrR[v])
        # advance until free for both ends
        while c in usedL[u] or c in usedR[v]:
            c += 1
        ans[idx] = c
        usedL[u].add(c)
        usedR[v].add(c)
        # move pointers forward
        if c >= ptrL[u]:
            ptrL[u] = c + 1
        if c >= ptrR[v]:
            ptrR[v] = c + 1

    out = ['YES', ' '.join(map(str, ans))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()