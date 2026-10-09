import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    nA = int(next(it))
    nB = int(next(it))
    m = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(m)]

    degA = [0] * nA
    degB = [0] * nB
    for u, v in edges:
        degA[u] += 1
        degB[v] += 1
    D = max(max(degA, default=0), max(degB, default=0))

    usedA = [set() for _ in range(nA)]
    usedB = [set() for _ in range(nB)]
    nxtA = [1] * nA
    nxtB = [1] * nB

    ans = [0] * m
    for idx, (u, v) in enumerate(edges):
        c = nxtA[u] if nxtA[u] > nxtB[v] else nxtB[v]
        # find first color not used at either endpoint
        while c in usedA[u] or c in usedB[v]:
            c += 1
        ans[idx] = c
        usedA[u].add(c)
        usedB[v].add(c)
        # advance next pointers
        while nxtA[u] in usedA[u]:
            nxtA[u] += 1
        while nxtB[v] in usedB[v]:
            nxtB[v] += 1

    # all colors are ≤ D by construction (Δ is the maximum degree)
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()