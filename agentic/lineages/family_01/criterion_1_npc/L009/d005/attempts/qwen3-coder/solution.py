from itertools import product

def determinant(u, v):
    # Matrix:
    # [1   1   1 ]
    # [cu  cv  4 ]
    # [cu^2 cv^2 16]
    #
    # Determinant = 1*(cv*16 - 4*cv^2) - 1*(cu*16 - 4*cu^2) + 1*(cu*cv^2 - cv*cu^2)
    #             = 16*cv - 4*cv^2 - 16*cu + 4*cu^2 + cu*cv^2 - cv*cu^2
    #             = 4*cu^2 - 16*cu - 4*cv^2 + 16*cv + cu*cv^2 - cv*cu^2
    #             = 4*(cu^2 - 4*cu - cv^2 + 4*cv) + cu*cv*(cv - cu)
    #             = 4*cu*(cu - 4) - 4*cv*(cv - 4) + cu*cv*(cv - cu)

    cu, cv = u, v
    det = 1 * (cv * 16 - 4 * cv * cv) - 1 * (cu * 16 - 4 * cu * cu) + 1 * (cu * cv * cv - cv * cu * cu)
    return det

def is_valid(c, constraints):
    for u, v in constraints:
        if determinant(c[u-1], c[v-1]) == 0:
            return False
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    constraints = []
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        constraints.append((u, v))
        idx += 2
    
    # Generate all possible sequences in lexicographical order
    for seq_tuple in product([1, 2, 3], repeat=n):
        seq = list(seq_tuple)
        if is_valid(seq, constraints):
            print("YES")
            print(' '.join(map(str, seq)))
            return
            
    print("NO")

if __name__ == "__main__":
    main()