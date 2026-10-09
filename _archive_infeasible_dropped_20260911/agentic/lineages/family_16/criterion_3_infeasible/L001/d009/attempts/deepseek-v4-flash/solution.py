import sys

def solve():
    input = sys.stdin.readline
    j, T = map(int, input().split())
    p1 = []
    p2 = []
    for _ in range(j):
        a, b = map(int, input().split())
        p1.append(a)
        p2.append(b)

    # Local contradiction check
    for i in range(j):
        if p1[i] + p2[i] > T:
            print(f"JOB {i+1}")
            return

    # Global contradiction check for c=1
    # Need to check if there is a cycle of length > T / p
    # Equivalent: sort by p, if max p * j > T? Actually need chain condition.
    # For c=1: V_i = U_i * 2^p_i, U_i >= 1, V_i <= 2^T
    # Pair condition: (V_i - U_k)(V_k - U_i) <= 0
    # This implies for any pair, one of V_i <= U_k or V_k <= U_i.
    # Since V_i > U_i, this forces a total order: U_a < V_a <= U_b < V_b <= ...
    # So if we sort by p ascending, the chain gives V_last >= 2^(sum of p's)
    # Need sum of all p's > T to be impossible.

    # For c=1
    if sum(p1) > T:
        print("LOAD 1")
        return

    # For c=2
    if sum(p2) > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    solve()