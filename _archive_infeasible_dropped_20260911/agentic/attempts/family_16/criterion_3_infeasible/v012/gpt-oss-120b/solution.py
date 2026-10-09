import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    j, T = data[0], data[1]
    sum1 = 0
    sum2 = 0
    bad_job = -1
    pos = 2
    for i in range(1, j + 1):
        p1 = data[pos]
        p2 = data[pos + 1]
        pos += 2
        if bad_job == -1 and p1 + p2 > T:
            bad_job = i
        sum1 += p1
        sum2 += p2

    if bad_job != -1:
        sys.stdout.write(f"JOB {bad_job}")
    elif sum1 > T:
        sys.stdout.write("LOAD 1")
    else:
        sys.stdout.write("LOAD 2")

if __name__ == "__main__":
    solve()