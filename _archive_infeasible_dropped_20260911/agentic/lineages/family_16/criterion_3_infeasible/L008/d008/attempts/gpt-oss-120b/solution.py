import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    p1_list = []
    p2_list = []
    sum_p1 = 0
    sum_p2 = 0
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        p1_list.append(p1)
        p2_list.append(p2)
        sum_p1 += p1
        sum_p2 += p2

    # Check JOB contradiction first
    twoT = 2 * T
    for idx, (p1, p2) in enumerate(zip(p1_list, p2_list), start=1):
        L1_2 = p1                     # = 2 * (p1/2)
        U1_2 = twoT - p1              # = 2 * (T - p1/2)
        L2_2 = p2
        U2_2 = twoT - p2
        D_2 = p1 + p2                 # = 2 * ((p1+p2)/2)
        # condition for impossibility: L1_2 > U2_2 - D_2
        if L1_2 > U2_2 - D_2:
            print(f"JOB {idx}")
            return

    # If no JOB, check LOAD contradictions
    if sum_p1 > T:
        print("LOAD 1")
    else:
        # sum_p2 must be > T for LOAD 2, otherwise problem guarantees one contradiction
        print("LOAD 2")

if __name__ == "__main__":
    solve()