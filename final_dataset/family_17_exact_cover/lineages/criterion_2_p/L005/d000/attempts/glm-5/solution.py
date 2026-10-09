import sys

def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0]); t = int(data[1])
    n = 2 * q
    if t == 0:
        print("NO" if q > 0 else "YES")
        return
    # parse edges
    # ...
    try:
        import numpy as np
        from scipy.sparse import csr_matrix
        from scipy.sparse.csgraph import maximum_bipartite_matching
        arr = np.array(data[2:2 + 2*t], dtype=np.int64)
        a = arr[0::2] - 1
        b = arr[1::2] - q - 1
        graph = csr_matrix((np.ones(t, dtype=np.int8), (a, b)), shape=(q, q))
        match = maximum_bipartite_matching(graph, perm_type='row_variables')
        if (match < 0).any():
            print("NO")
        else:
            out = ["YES"]
            for i in range(q):
                out.append(f"{i+1} {match[i]+q+1}")
            sys.stdout.write("\n".join(out) + "\n")
    except ImportError:
        # fallback pure python HK
        ...