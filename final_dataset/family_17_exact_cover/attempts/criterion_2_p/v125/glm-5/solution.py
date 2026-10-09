try:
    from scipy.sparse.csgraph import maximum_bipartite_matching
    from scipy.sparse import csr_matrix
    # use it
except ImportError:
    # pure python HK