import sys

def main():
    input = sys.stdin.readline
    j, T = map(int, input().split())
    q1 = []
    q2 = []
    for _ in range(j):
        a, b = map(int, input().split())
        q1.append(a)
        q2.append(b)

    # Check JOB condition
    for i in range(j):
        # w1 >= q1, w2 <= 2T - q2, w2 - w1 >= q1 + q2
        # Minimal w2 = w1 + q1 + q2 >= q1 + q1 + q2 = 2*q1 + q2
        # Need 2*q1 + q2 <= 2T - q2  => 2*q1 + 2*q2 <= 2T => q1 + q2 <= T
        if q1[i] + q2[i] > T:
            print(f"JOB {i+1}")
            return

    # Check LOAD 1
    # Need to see if we can place j points with min distance q1[i]+q1[k]
    # within [q1[i], 2T - q1[i]] for each i
    # Equivalent: sort by q1, check if total required span > available
    # For LOAD c, the allowed interval for each i is [q_c[i], 2T - q_c[i]]
    # The maximum possible leftmost is max(q_c), rightmost is min(2T - q_c)
    # But dispersion requires pairwise distances >= q_c[i] + q_c[k]
    # A known necessary and sufficient condition for 1D packing with variable sizes:
    # Sort by q_c, then check if for all i, sum of previous q_c + current q_c <= span
    # More precisely: if sorted q_c ascending, need for all i:
    # q_c[i] + sum_{k<i} 2*q_c[k] <= 2T - q_c[i]  (placing from left)
    # Actually simpler: The minimal span needed is:
    # max(q_c) + sum of all other q_c (each contributes at least q_c[i]+q_c[k] distance)
    # But we can do greedy: place first at leftmost, then each next at previous + q_c[prev]+q_c[cur]
    # Check if fits within rightmost bound.

    for c in [1, 2]:
        q = q1 if c == 1 else q2
        # Sort by q
        idx = sorted(range(j), key=lambda x: q[x])
        # Place first at its leftmost
        pos = q[idx[0]]
        ok = True
        for t in range(1, j):
            prev = idx[t-1]
            cur = idx[t]
            pos = pos + q[prev] + q[cur]
            if pos > 2*T - q[cur]:
                ok = False
                break
        if not ok:
            print(f"LOAD {c}")
            return

    # Should not reach here per problem guarantee
    print("JOB 1")

if __name__ == "__main__":
    main()