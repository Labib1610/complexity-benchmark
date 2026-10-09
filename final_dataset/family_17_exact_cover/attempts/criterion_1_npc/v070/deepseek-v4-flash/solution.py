import sys
sys.setrecursionlimit(1000000)



def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3*q
    triples = []
    person_triples_mask = [0]*n
    for i in range(t):
        a = int(next(it))-1
        b = int(next(it))-1
        c = int(next(it))-1
        triples.append((a,b,c))
        mask = (1<<a) | (1<<b) |(1<<c)
        # store mask? We'll compute later
        person_triples_mask[a] |= 1<<i
        person_triples_mask[b] |= 1<<i
        person_triples_mask[c] |= 1<<i
    # compute person_mask for each triple
    person_mask = [0]*t
    intersect_mask = [0]*t
    for i,(a,b,c) in enumerate(triples):
        pm = (1<<a) |(1<<b) |(1<<c)
        person_mask[i] = pm
        intersect_mask[i] = person_triples_mask[a] | person_triples_mask[b] | person_triples_mask[c]
    full_persons = (1<<n) - 1
    full_triples = (1<<t) - 1
    chosen = []
    def dfs(remaining, available):
        if remaining == 0:
            return True
        # find best person
        best_p = -1
        best_cnt = t+1
        temp = remaining
        while temp:
            lsb = temp & -temp
            p = lsb.bit_length() - 1
            cnt = (available & person_triples_mask[p]).bit_count()
            if cnt == 0:
                return False
            if cnt < best_cnt:
                best_cnt = cnt
                best_p = p
                if cnt == 1:
                    break
            temp -= lsb
        # try triples
        triples_mask = available & person_triples_mask[best_p]
        while triples_mask:
            lsb = triples_mask & -triples_mask
            tri = lsb.bit_length() - 1
            chosen.append(tri)
            if dfs(remaining & ~person_mask[tri], available & ~intersect_mask[tri]):
                return True
            chosen.pop()
            triples_mask -= lsb
        return False
    if dfs(full_persons, full_triples):
        out = ["YES"]
        for tri in chosen:
            a,b,c = triples[tri]
            out.append(f"{a+1} {b+1} {c+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()