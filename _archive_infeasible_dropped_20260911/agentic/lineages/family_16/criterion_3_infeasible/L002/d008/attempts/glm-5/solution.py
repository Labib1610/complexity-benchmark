import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    p1 = [0] * (j + 1)
    p2 = [0] * (j + 1)
    idx = 2
    for i in range(1, j + 1):
        p1[i] = int(data[idx])
        p2[i] = int(data[idx + 1])
        idx += 2

    # JOB certificate: u_i >= p1_i, v_i - u_i >= p1_i + p2_i, v_i <= 2T - p2_i
    # => v_i >= u_i + p1_i + p2_i >= p1_i + p1_i + p2_i = 2*p1_i + p2_i
    # Need 2*p1_i + p2_i <= 2T - p2_i  =>  2*p1_i + 2*p2_i <= 2T  =>  p1_i + p2_i <= T
    # JOB i is valid when p1_i + p2_i > T
    for i in range(1, j + 1):
        if p1[i] + p2[i] > T:
            sys.stdout.write(f"JOB {i}\n")
            return

    # LOAD 1 certificate: u_i >= p1_i, u_i <= 2T - p1_i, |u_i - u_k| >= p1_i + p1_k
    # Equivalent to placing intervals [p1_i, 2T - p1_i] with separation p1_i + p1_k
    # Sort by p1_i; check if sum of p1_i + p1_{i+1} exceeds 2T - p1_1 - p1_n
    order = sorted(range(1, j + 1), key=lambda i: p1[i])
    total = 0
    for k in range(j - 1):
        i = order[k]
        nxt = order[k + 1]
        total += p1[i] + p1[nxt]
    first = order[0]
    last = order[-1]
    if total > 2 * T - p1[first] - p1[last]:
        sys.stdout.write("LOAD 1\n")
        return

    # LOAD 2 certificate: v_i >= p2_i, v_i <= 2T - p2_i, |v_i - v_k| >= p2_i + p2_k
    order = sorted(range(1, j + 1), key=lambda i: p2[i])
    total = 0
    for k in range(j - 1):
        i = order[k]
        nxt = order[k + 1]
        total += p2[i] + p2[nxt]
    first = order[0]
    last = order[-1]
    if total > 2 * T - p2[first] - p2[last]:
        sys.stdout.write("LOAD 2\n")
        return

if __name__ == "__main__":
    main()