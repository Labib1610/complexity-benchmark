def can_assign(shifts, restrictions, n):
    for i in range(n):
        if shifts[i] == 0:
            valid = True
            for j in range(n):
                if (i + 1, j + 1) in restrictions or (j + 1, i + 1) in restrictions:
                    if shifts[j] == shifts[i]:
                        valid = False
                        break
            if valid:
                return True
    return False

def dfs(shifts, restrictions, n):
    for i in range(1, 4):
        if can_assign(shifts, restrictions, n):
            return True, shifts
        shifts[i - 1] = i
        exists, result_shifts = dfs(shifts, restrictions, n)
        if exists:
            return True, result_shifts
        shifts[i - 1] = 0

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    restrictions = set()
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        restrictions.add((u, v))
        idx += 2

    shifts = [0] * n
    exists, result_shifts = dfs(shifts, restrictions, n)
    
    if not exists:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, result_shifts)))