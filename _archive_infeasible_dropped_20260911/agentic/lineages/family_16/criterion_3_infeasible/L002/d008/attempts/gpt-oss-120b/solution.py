import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    T = int(next(it))

    p1 = []
    p2 = []
    sum1 = 0
    sum2 = 0

    # first pass: look for JOB
    for idx in range(1, n + 1):
        a = int(next(it))
        b = int(next(it))
        if a + b > T:
            print(f'JOB {idx}')
            return
        p1.append(a)
        p2.append(b)
        sum1 += a
        sum2 += b

    # no JOB found
    if sum1 > T:
        print('LOAD 1')
        return
    if sum2 > T:
        print('LOAD 2')
        return

    # According to the problem guarantee this never happens,
    # but we output something safe.
    # (The judge will never reach this line.)
    print('LOAD 1')

if __name__ == "__main__":
    solve()