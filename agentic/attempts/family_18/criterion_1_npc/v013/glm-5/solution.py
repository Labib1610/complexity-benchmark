import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    deg = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        deg[u] += 1
        deg[v] += 1

    # Sort modules by degree descending; ties broken by module id.
    modules = list(range(1, n + 1))
    modules.sort(key=lambda x: (-deg[x], x))

    # Assign slots from the center outward.
    slots = [0] * (n + 1)
    lo, hi = (n + 1) // 2, (n + 1) // 2
    if n % 2 == 0:
        lo = n // 2
        hi = lo + 1

    left_turn = True
    for mod in modules:
        if left_turn:
            slots[mod] = lo
            lo -= 1
        else:
            slots[mod] = hi
            hi += 1
        left_turn = not left_turn

    out = ["YES", " ".join(str(slots[i]) for i in range(1, n + 1))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()