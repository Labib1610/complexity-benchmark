import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N_emp = int(next(it))
    N_ven = int(next(it))
    M = int(next(it))
    edges = [(int(next(it)) - 1, int(next(it)) - 1) for _ in range(M)]

    deg_emp = [0] * N_emp
    deg_ven = [0] * N_ven
    for u, v in edges:
        deg_emp[u] += 1
        deg_ven[v] += 1
    F = max(max(deg_emp, default=0), max(deg_ven, default=0))

    used_emp = [set() for _ in range(N_emp)]
    used_ven = [set() for _ in range(N_ven)]
    nxt_emp = [1] * N_emp  # next candidate color for each employee

    ans = [0] * M
    for idx, (u, v) in enumerate(edges):
        c = nxt_emp[u]
        # find a color not used by vendor v
        while c in used_ven[v]:
            c += 1
        # assign
        ans[idx] = c
        used_emp[u].add(c)
        used_ven[v].add(c)
        # update next candidate for employee u
        while nxt_emp[u] in used_emp[u]:
            nxt_emp[u] += 1

    out = ['YES', ' '.join(map(str, ans))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()