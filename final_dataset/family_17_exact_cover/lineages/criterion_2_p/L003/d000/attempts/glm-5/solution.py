def try_kuhn_iterative(root, adj, match_left, match_right, dist):
    # iterative DFS
    stack = [root]
    path = []  # track vertices on path
    ...