from itertools import product

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build proximity matrix P
    P = [[0]*n for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        P[u][v] = 1
        P[v][u] = 1
        idx += 2

    # Try all possible assignments in lexicographical order
    for assignment in product([1,2,3], repeat=n):
        # Construct state matrix S (n x 3)
        S = [[0]*3 for _ in range(n)]
        for i in range(n):
            S[i][assignment[i]-1] = 1
        
        # Compute S^T * P * S
        # First compute P * S -> n x 3 matrix
        PS = [[0]*3 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if P[i][j] == 1:
                    for k in range(3):
                        PS[i][k] += S[j][k]
        
        # Then compute S^T * (P * S) -> 3 x 3 matrix
        STPS = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(n):
                    STPS[i][j] += S[k][i] * PS[k][j]
        
        # Check if diagonal is all zeros
        valid = True
        for i in range(3):
            if STPS[i][i] != 0:
                valid = False
                break
        
        if valid:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    print("NO")

if __name__ == "__main__":
    main()