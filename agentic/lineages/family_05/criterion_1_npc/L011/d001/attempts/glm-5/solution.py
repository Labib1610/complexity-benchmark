import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    vectors = []
    idx = 2
    for _ in range(t):
        x = int(data[idx]) - 1
        y = int(data[idx+1]) - 1
        z = int(data[idx+2]) - 1
        vectors.append((x, y, z))
        idx += 3

    # Group vectors by x (pulsar frequency)
    by_x = [[] for _ in range(k)]
    for i, (x, y, z) in enumerate(vectors):
        by_x[x].append(i)

    # Order x's by ascending number of candidate vectors (heuristic)
    x_order = sorted(range(k), key=lambda x: len(by_x[x]))

    y_used = [False] * k
    z_used = [False] * k
    chosen = [-1] * k

    def backtrack(pos):
        if pos == k:
            return True
        x = x_order[pos]
        for vi in by_x[x]:
            _, y, z = vectors[vi]
            if not y_used[y] and not z_used[z]:
                y_used[y] = True
                z_used[z] = True
                chosen[x] = vi
                if backtrack(pos + 1):
                    return True
                y_used[y] = False
                z_used[z] = False
                chosen[x] = -1
        return False

    if backtrack(0):
        out = ["YES"]
        for x in range(k):
            vi = chosen[x]
            vx, vy, vz = vectors[vi]
            out.append(f"{vx+1} {vy+1} {vz+1}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

solve()