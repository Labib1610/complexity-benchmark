import sys


def main():
    sys.setrecursionlimit(10000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    w = [int(data[idx + i]) for i in range(n)]; idx += n

    order = sorted(range(n), key=lambda i: -w[i])

    def fits(kk):
        """Can the items be packed into kk containers of capacity C? Returns an assignment or None.
        Heaviest-first backtracking with the empty-container symmetry cut."""
        load = [0] * kk
        assign = [0] * n

        def solve(pos):
            if pos == n:
                return True
            i = order[pos]; wi = w[i]
            for b in range(kk):
                if load[b] + wi <= C:
                    load[b] += wi; assign[i] = b + 1
                    if solve(pos + 1):
                        return True
                    load[b] -= wi
                if load[b] == 0:
                    break
            return False

        return assign if solve(0) else None

    total = sum(w)
    lb = (total + C - 1) // C            # ceil(total / C): a valid lower bound on the container count
    lb = max(1, lb)
    for kk in range(lb, n + 1):
        a = fits(kk)
        if a is not None:
            sys.stdout.write(f"{kk}\n")
            sys.stdout.write(" ".join(map(str, a)) + "\n")
            return


main()
