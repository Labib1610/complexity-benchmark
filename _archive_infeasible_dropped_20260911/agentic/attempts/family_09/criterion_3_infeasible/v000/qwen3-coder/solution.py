n, m, k = map(int, input().split())

if k > n:
    print("SIZE")
else:
    # Check if the graph is complete
    # A complete graph with n nodes has n*(n-1)/2 edges
    if m == n * (n - 1) // 2 and k >= 2:
        print("COMPLETE")
    else:
        # This shouldn't happen according to the problem statement,
        # but we'll handle it just in case
        print("SIZE")