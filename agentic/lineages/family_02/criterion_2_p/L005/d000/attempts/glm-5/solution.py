import sys
import numpy as np

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    N = 2 * n
    if m == 0:
        # all zeros is valid
        sys.stdout.write("YES\n" + " ".join(["0"] * n) + "\n")
        return
    # parse literals
    L = np.array(list(map(int, data[2:2 + 2*m])), dtype=np.int64)
    # nodes
    neg_mask = L < 0
    al = np.abs(L)
    nodes = 2*al - 2 + neg_mask   # dtype bool→int64? 2*al-2 is int64, neg_mask bool broadcasts to int64. Actually int64 + bool → int64. OK.
    a = nodes[0::2]
    b = nodes[1::2]
    eu = np.concatenate([a ^ 1, b ^ 1])
    ev = np.concatenate([b, a])
    # CSR
    counts = np.bincount(eu, minlength=N)
    start_np = np.zeros(N + 1, dtype=np.int64)
    np.cumsum(counts, out=start_np[1:])
    order_idx = np.argsort(eu, kind='stable')
    adj = ev[order_idx].tolist()
    start = start_np.tolist()
    
    # Tarjan iterative
    index = [-1] * N
    low = [0] * N
    comp = [-1] * N
    on_st = bytearray(N)
    it = start[:N]  # copy of first N entries; it[v] = current pointer
    scc_stack = []
    scc_append = scc_stack.append
    scc_pop = scc_stack.pop
    call_stack = []
    call_append = call_stack.append
    call_pop = call_stack.pop
    counter = 0
    comp_cnt = 0
    
    for s in range(N):
        if index[s] != -1:
            continue
        call_append(s)
        while call_stack:
            v = call_stack[-1]
            if index[v] == -1:
                index[v] = counter
                low[v] = counter
                counter += 1
                scc_append(v)
                on_st[v] = 1
            i = it[v]
            end_v = start[v + 1]
            advanced = False
            while i < end_v:
                w = adj[i]
                i += 1
                iw = index[w]
                if iw == -1:
                    it[v] = i
                    call_append(w)
                    advanced = True
                    break
                elif on_st[w] and iw < low[v]:
                    low[v] = iw
            if advanced:
                continue
            it[v] = i
            call_pop()
            cs = call_stack
            if cs:
                p = cs[-1]
                lv = low[v]
                if lv < low[p]:
                    low[p] = lv
            if low[v] == index[v]:
                while True:
                    w = scc_pop()
                    on_st[w] = 0
                    comp[w] = comp_cnt
                    if w == v:
                        break
                comp_cnt += 1
    ...