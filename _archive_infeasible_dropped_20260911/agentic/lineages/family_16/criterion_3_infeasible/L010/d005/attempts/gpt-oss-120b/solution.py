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
    # Check causality while reading
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 + p2 > T:
            print(f"JOB {idx}")
            return
        p1_list.append(p1)
        p2_list.append(p2)
    # No causality failure, check query independence
    if sum(p1_list) > T:
        print("LOAD 1")
        return
    # Check reply independence
    if sum(p2_list) > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    solve()