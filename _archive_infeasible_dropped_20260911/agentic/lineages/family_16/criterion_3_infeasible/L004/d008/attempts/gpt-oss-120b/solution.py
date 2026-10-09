import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    sum1 = 0
    sum2 = 0
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        # check job-specific impossibility
        if p1 > T or p2 > T or p1 + p2 > T:
            sys.stdout.write(f"JOB {idx}")
            return
        sum1 += p1
        sum2 += p2
    # no job contradiction, check collection contradictions
    if sum1 > T:
        sys.stdout.write("LOAD 1")
    else:
        # by problem guarantee one certificate exists, so sum2 must exceed T
        sys.stdout.write("LOAD 2")

if __name__ == "__main__":
    solve()