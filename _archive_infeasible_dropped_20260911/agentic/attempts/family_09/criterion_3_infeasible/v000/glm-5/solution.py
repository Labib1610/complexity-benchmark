import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    if k > n:
        print("SIZE")
        return
    
    # Check if graph is complete: m == n*(n-1)//2
    # Since guaranteed one of the two reasons applies and k <= n here,
    # the graph must be complete.
    print("COMPLETE")

if __name__ == "__main__":
    main()