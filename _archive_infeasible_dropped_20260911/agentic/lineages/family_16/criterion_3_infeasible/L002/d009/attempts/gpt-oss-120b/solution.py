import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))

    q1 = []
    q2 = []

    # first pass: look for JOB
    for idx in range(1, j + 1):
        a = int(next(it))
        b = int(next(it))
        q1.append(a)
        q2.append(b)
        if a + b > T:
            print(f"JOB {idx}")
            return

    # no JOB, try LOAD 1
    # find two largest q1
    mx1 = mx2 = -1
    for v in q1:
        if v > mx1:
            mx2 = mx1
            mx1 = v
        elif v > mx2:
            mx2 = v
    if mx1 + mx2 > T:
        print("LOAD 1")
        return

    # otherwise LOAD 2 must work
    mx1 = mx2 = -1
    for v in q2:
        if v > mx1:
            mx2 = mx1
            mx1 = v
        elif v > mx2:
            mx2 = v
    # by problem guarantee this condition holds
    print("LOAD 2")

if __name__ == "__main__":
    solve()