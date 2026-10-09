from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
# map A vertices to rows 0..|A|-1, B to cols 0..|B|-1
# build csr with edges
match = maximum_bipartite_matching(csr, perm_type='row')  # array size |A|