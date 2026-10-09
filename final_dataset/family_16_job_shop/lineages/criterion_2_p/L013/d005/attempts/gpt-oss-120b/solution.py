import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    A = []  # p1 <= p2
    B = []  # p1 > p2
    for _ in range(n):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 <= p2:
            A.append((p1, p2))
        else:
            B.append((p1, p2))
    A.sort(key=lambda x: x[0])          # increasing p1
    B.sort(key=lambda x: -x[1])         # decreasing p2
    seq = A + B

    cur_time = 0          # current finish time of processing unit
    arrival = 0           # cumulative arrival time
    for p1, p2 in seq:
        arrival += p1
        start = max(arrival, cur_time)
        cur_time = start + p2
    print(cur_time)

if __name__ == "__main__":
    solve()