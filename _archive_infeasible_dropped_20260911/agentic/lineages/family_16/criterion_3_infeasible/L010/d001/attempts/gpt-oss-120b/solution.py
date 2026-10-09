import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    p1_list = []
    p2_list = []
    sum1 = 0
    sum2 = 0
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        p1_list.append(p1)
        p2_list.append(p2)
        sum1 += p1
        sum2 += p2

    if sum1 > T:
        sys.stdout.write("LOAD 1")
        return
    if sum2 > T:
        sys.stdout.write("LOAD 2")
        return

    for idx, (p1, p2) in enumerate(zip(p1_list, p2_list), start=1):
        if p1 + p2 > T:
            sys.stdout.write(f"JOB {idx}")
            return

if __name__ == "__main__":
    solve()