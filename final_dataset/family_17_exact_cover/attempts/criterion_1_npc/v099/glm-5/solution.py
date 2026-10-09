import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    n = 3 * q
    
    triples = []
    for _ in range(t):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        c = int(input_data[idx]); idx += 1
        triples.append((a, b, c))
    
    # element -> list of triple indices
    elem_triples = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triples):
        elem_triples[a].append(i)
        elem_triples[b].append(i)
        elem_triples[c].append(i)
    
    covered = [False] * (n + 1)
    used = [False] * t
    chosen = []
    
    # iterative backtracking with MRV
    def find_mrv():
        best = -1
        best_count = 10**9
        for e in range(1, n + 1):
            if covered[e]:
                continue
            cnt = 0
            for ti in elem_triples[e]:
                if not used[ti]:
                    cnt += 1
            if cnt == 0:
                return -2  # dead end
            if cnt < best_count:
                best_count = cnt
                best = e
                if cnt == 1:
                    return e
        return best
    
    # recursive
    sys.setrecursionlimit(10000)
    
    def backtrack(depth):
        if depth == q:
            return True
        e = find_mrv()
        if e < 0:
            return False
        for ti in elem_triples[e]:
            if used[ti]:
                continue
            a, b, c = triples[ti]
            if covered[a] or covered[b] or covered[c]:
                continue
            # choose
            used[ti] = True
            covered[a] = covered[b] = covered[c] = True
            chosen.append(triples[ti])
            if backtrack(depth + 1):
                return True
            # undo
            chosen.pop()
            covered[a] = covered[b] = covered[c] = False
            used[ti] = False
        return False
    
    if backtrack(0):
        out = ["YES"]
        for tr in chosen:
            out.append(f"{tr[0]} {tr[1]} {tr[2]}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()