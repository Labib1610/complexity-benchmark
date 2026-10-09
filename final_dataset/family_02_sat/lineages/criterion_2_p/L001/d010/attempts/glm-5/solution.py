import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    # nodes: 0..2n-1. node 2i = X_{i+1} true, 2i+1 = X_{i+1} false.
    # edges as CSR
    ef = [0] * (2 * m)  # edge from
    et = [0] * (2 * m)  # edge to
    cnt = 0
    for _ in range(m):
        l1 = int(input_data[idx]); idx += 1
        l2 = int(input_data[idx]); idx += 1
        u = abs(l1) - 1  # 0-based hub index
        v = abs(l2) - 1
        # literal "s_u = a" where a = 1 if l1 < 0 else 0
        # a=1 -> node 2u (X true), a=0 -> node 2u+1 (X false)
        if l1 < 0:
            p = 2 * u
        else:
            p = 2 * u + 1
        if l2 < 0:
            q = 2 * v
        else:
            q = 2 * v + 1
        # edges: p -> q^1, q -> p^1
        ef[cnt] = p; et[cnt] = q ^ 1; cnt += 1
        ef[cnt] = q; et[cnt] = p ^ 1; cnt += 1
    ...