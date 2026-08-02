from itertools import permutations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    conflicts = [(int(data[i*2+2])-1, int(data[i*2+3])-1) for i in range(m)]
    
    def is_valid(shifts):
        for u, v in conflicts:
            if shifts[u] == shifts[v]:
                return False
        return True
    
    for perm in permutations([1, 2, 3], n):
        valid = True
        for u, v in conflicts:
            if perm[u] == perm[v]:
                valid = False
                break
        if valid:
            print("YES")
            print(*perm)
            return
    
    print("NO")

solve()