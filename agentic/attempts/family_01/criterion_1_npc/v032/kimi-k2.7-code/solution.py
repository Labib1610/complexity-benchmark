```python
import sys

def solve():
    sys.setrecursionlimit(1000000)
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # quick check: a K4 is never 3-colorable
    def has_k4():
        for u in range(n):
            au = adj[u]
            vmask = au >> (u + 1)
            while vmask:
                lsb = vmask & -vmask
                v = (u + 1) + (lsb.bit_length() - 1)
                vmask ^= lsb
                common = au & adj[v]
                cmask = common
                while cmask:
                    lsb2 = cmask & -cmask
                    w = lsb2.bit_length() - 1
                    cmask ^= lsb2
                    if (adj[w] & common) & ~(1 << w):
                        return True
        return False

    if has_k4():
        print("NO")
        return

    def can_complete(colors):
        """Return True iff the partial coloring in colors (0=uncolored,1..3) extends."""
        allowed = [0] * n
        active_mask = 0
        for v in range(n):
            c = colors[v]
            if c:
                allowed[v] = 1 << c
            else:
                mask = 0b1110
                nb = adj[v]
                while nb:
                    lsb = nb & -nb
                    u = lsb.bit_length()