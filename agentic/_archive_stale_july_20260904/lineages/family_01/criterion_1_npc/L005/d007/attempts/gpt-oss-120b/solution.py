import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u].add(v)
        adj[v].add(u)

    # colour: -1 = uncoloured, otherwise 0,1,2   (0->1, 1->2, 2->3)
    colour = [-1] * n
    # mask[v]: bit i set means colour i still possible
    mask = [0b111] * n

    # stack of modifications for backtracking:
    # each element is (vertex, old_mask, old_colour)
    stack = []

    def assign(v: int, c: int) -> bool:
        """assign colour c to vertex v, propagate, return False on contradiction"""
        # remember old state of v
        stack.append((v, mask[v], colour[v]))
        colour[v] = c
        mask[v] = 1 << c

        for nb in adj[v]:
            if colour[nb] == -1:
                if mask[nb] & (1 << c):
                    old = mask[nb]
                    stack.append((nb, old, -1))
                    mask[nb] = old & ~(1 << c)
                    if mask[nb] == 0:
                        return False
            else:
                if colour[nb] == c:      # neighbour already has same colour
                    return False
        return True

    def undo(to: int) -> None:
        """revert stack to length 'to'"""
        while len(stack) > to:
            v, old_mask, old_colour = stack.pop()
            mask[v] = old_mask
            colour[v] = old_colour

    def dfs(pos: int) -> bool:
        """try to colour vertices pos .. n-1 (in natural order)"""
        if pos == n:
            return True
        # try colours 0,1,2 (i.e. frequencies 1,2,3) in increasing order
        for c in range(3):
            if mask[pos] & (1 << c):
                checkpoint = len(stack)
                if assign(pos, c):
                    if dfs(pos + 1):
                        return True
                undo(checkpoint)
        return False

    possible = dfs(0)

    if not possible:
        sys.stdout.write("NO\n")
        return

    # translate colours 0,1,2 -> frequencies 1,2,3
    freq = [str(colour[i] + 1) for i in range(n)]
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(freq) + "\n")


if __name__ == "__main__":
    solve()