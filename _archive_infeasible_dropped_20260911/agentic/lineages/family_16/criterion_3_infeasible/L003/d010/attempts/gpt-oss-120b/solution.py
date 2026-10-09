import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    T = int(next(it))
    p1 = [0] * n
    p2 = [0] * n
    for i in range(n):
        p1[i] = int(next(it))
        p2[i] = int(next(it))

    # 1) look for contradictory JOB
    for i in range(n):
        if p1[i] > T or p1[i] + p2[i] > T:
            sys.stdout.write(f"JOB {i+1}\n")
            return

    # no JOB fails -> contradiction is in a class
    def class_feasible(params):
        params.sort()
        prev_sum = None
        prev_p = None
        for p in params:
            low = p
            high = 2 * T - p
            if prev_sum is None:
                cur = low
            else:
                cur = max(low, prev_sum + prev_p + p)
            if cur > high:
                return False
            prev_sum = cur
            prev_p = p
        return True

    if not class_feasible(p1[:]):          # class 1
        sys.stdout.write("LOAD 1\n")
    else:
        # class 2 must be contradictory
        sys.stdout.write("LOAD 2\n")

if __name__ == "__main__":
    solve()