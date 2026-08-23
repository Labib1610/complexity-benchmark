import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        neighbors[u].append(v)
        neighbors[v].append(u)

    # Turan's theorem: a 3-colorable graph has at most floor(n^2/3) edges.
    if m > n * n // 3:
        sys.stdout.write("NO")
        return

    FULL = 7          # bits for colors 1,2,3
    SINGLE = (1, 2, 4)

    sys.setrecursionlimit(10000)
    assignment = [0] * n

    def propagate(domains):
        """Apply unit propagation; return False if a domain becomes empty."""
        inq = [False] * n
        stack = [i for i, d in enumerate(domains) if d in SINGLE]
        for i in stack:
            inq[i] = True
        while stack:
            v = stack.pop()
            inq[v] = False
            col = domains[v]
            for w in neighbors[v]:
                if domains[w] & col:
                    domains[w] &= ~col
                    nd = domains[w]
                    if nd == 0:
                        return False
                    if nd in SINGLE and not inq[w]:
                        stack.append(w)
                        inq[w] = True
        return True

    def dfs(pos, domains):
        if pos == n:
            for i in range(n):
                assignment[i] = domains[i].bit_length()
            return True
        d = domains[pos]
        if d == 0:
            return False
        if d in SINGLE:
            return dfs(pos + 1, domains)
        for cbit in (1, 2, 4):
            if d & cbit:
                newdom = domains[:]
                newdom[pos] = cbit
                if propagate(newdom):
                    if dfs(pos + 1, newdom):
                        return True
        return False

    # The lexicographically smallest coloring can always have technician 1 in phase 1.
    domains = [FULL] * n
    domains[0] = 1
    if not propagate(domains):
        sys.stdout.write("NO")
        return
    if not dfs(1, domains):
        sys.stdout.write("NO")
        return

    out = ["YES", " ".join(map(str, assignment))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()