from itertools import combinations

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    
    det = 0
    for col in range(n):
        submatrix = [[matrix[i][j] for j in range(n) if j != col] for i in range(1, n)]
        det += ((-1) ** col) * matrix[0][col] * determinant(submatrix)
    return det

def is_valid_selection(relays, k):
    # Create primary channel matrix
    primary_matrix = [[0] * k for _ in range(k)]
    for i in range(k):
        primary_matrix[i][relays[i][0] - 1] = 1
    
    # Create secondary channel matrix
    secondary_matrix = [[0] * k for _ in range(k)]
    for i in range(k):
        secondary_matrix[i][relays[i][1] - 1] = 1
    
    # Create tertiary channel matrix
    tertiary_matrix = [[0] * k for _ in range(k)]
    for i in range(k):
        tertiary_matrix[i][relays[i][2] - 1] = 1
    
    # Check if all determinants are non-zero
    return (determinant(primary_matrix) != 0 and 
            determinant(secondary_matrix) != 0 and 
            determinant(tertiary_matrix) != 0)

def solve():
    k, t = map(int, input().split())
    
    if k == 0:
        print("YES")
        return
    
    if t < k:
        print("NO")
        return
    
    relays = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        relays.append((a, b, c))
    
    # Try all combinations of k relays
    for combination in combinations(relays, k):
        if is_valid_selection(combination, k):
            print("YES")
            for relay in combination:
                print(relay[0], relay[1], relay[2])
            return
    
    print("NO")

solve()