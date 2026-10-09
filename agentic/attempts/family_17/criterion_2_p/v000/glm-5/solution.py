from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
graph = csr_matrix((ones, (rows, cols)), shape=(q, q))
matching = maximum_bipartite_matching(graph, perm_type='column')
# matching[i] = j means row i matched to column j, or -1 if unmatched