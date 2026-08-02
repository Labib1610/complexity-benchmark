import sys


def main():
    sys.setrecursionlimit(10000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    w = [int(data[idx + i]) for i in range(n)]; idx += n

    # Backtracking: place items heaviest-first (strong pruning). Each item goes
    # into the lowest-load feasible container; a symmetry cut stops us from
    # trying more than one currently-empty container (they are interchangeable).
    order = sorted(range(n), key=lambda i: -w[i])
    load = [0] * k
    assign = [0] * n

    def solve(pos):
        if pos == n:
            return True
        i = order[pos]
        wi = w[i]
        for b in range(k):
            if load[b] + wi <= C:
                load[b] += wi
                assign[i] = b + 1
                if solve(pos + 1):
                    return True
                load[b] -= wi
            if load[b] == 0:
                # first empty container failed → all further empties are equivalent
                break
        return False

    if solve(0):
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, assign)) + "\n")
    else:
        sys.stdout.write("NO\n")


main()
