import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    if k > n:
        print("SIZE")
        return
    
    # For a complete graph, m must equal n*(n-1)//2
    if m == n * (n - 1) // 2:
        print("COMPLETE")
    else:
        # According to the problem, one of the two reasons always applies.
        # If not SIZE and not COMPLETE, we still need to output something.
        # But the statement guarantees one of them holds.
        # We can fallback to COMPLETE if k >= 2 and graph is complete.
        # If k == 1, COMPLETE is not needed, but problem says k >= 1.
        # For k == 1, a group always exists, so this case shouldn't appear.
        # We'll just print COMPLETE as a safe fallback.
        print("COMPLETE")

if __name__ == "__main__":
    main()