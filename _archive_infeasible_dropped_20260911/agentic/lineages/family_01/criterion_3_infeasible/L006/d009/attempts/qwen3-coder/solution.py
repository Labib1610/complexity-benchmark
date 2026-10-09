import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    pulses = []
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        pulses.append((u, v))
        idx += 2
    
    # Initialize state vectors
    V = [[0]*m for _ in range(n+1)]
    
    # Process each pulse
    for k in range(m):
        u, v = pulses[k]
        V[u][k] = 1
        V[v][k] = 1
    
    # Compute all pairwise dot products
    dot = [[0]*(n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(i, n+1):
            res = 0
            for k in range(m):
                res += V[i][k] * V[j][k]
            dot[i][j] = res
            dot[j][i] = res
    
    # Find the lexicographically smallest triplet
    for x1 in range(1, n-1):
        for x2 in range(x1+1, n):
            if dot[x1][x2] == 0:
                continue
            for x3 in range(x2+1, n+1):
                if dot[x1][x3] == 0 or dot[x2][x3] == 0:
                    continue
                print(x1, x2, x3)
                return

if __name__ == "__main__":
    main()