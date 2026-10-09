import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    n = 3*q
    triads_by_first = [[] for _ in range(n+1)]
    for _ in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        triads_by_first[a].append((b,c))
    # Optional: sort each list by b then c? Not needed.
 But we can sort to have deterministic order.
    for lst in triads_by_first:
        lst.sort()
    chosen = []
    failed = set()
    def dfs(mask, count):
        if count == q:
            return True
        if mask in failed:
            return False
        # find smallest unused
        # We can compute by iterating; n<=600, fine.
        first = None
        # We can optimize by maintaining next_unused? But mask changes; we can compute quickly using bit operations? Python int bit_length? We can do:
        # We can find first zero bit: ~mask & ((1<<(n+1))-1) then lowbit. But n<=600, simple loop fine.
        for i in range(1, n+1):
            if not (mask >> i) & 1:
                first = i
                break
        if first is None:
            return False
        for b,c in triads_by_first[first]:
            if (mask >> b) & 1 or (mask >> c) & 1:
                continue
            newmask = mask | (1 << first) | (1 << b) | (1 << c)
            chosen.append((first,b,c))
            if dfs(newmask, count+1):
                return True
            chosen.pop()
        failed.add(mask)
        return False
    if dfs(0,0):
        out = ["YES"]
        for a,b,c in chosen:
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

if __name__ == "__main__":
    solve()