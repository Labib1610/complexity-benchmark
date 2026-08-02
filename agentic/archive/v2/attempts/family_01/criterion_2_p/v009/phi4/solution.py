from sys import stdin, stdout

def main():
    input = stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    conflicts = [[] for _ in range(n)]
    
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        idx += 2
        conflicts[u].append(v)
        conflicts[v].append(u)
    
    shifts = [0] * n
    
    def is_valid(shifts, worker, shift):
        for neighbor in conflicts[worker]:
            if shifts[neighbor] == shift:
                return False
        return True

    def assign_shifts(worker, shift1=True):
        if shifts[worker] != 0:
            return
        
        current_shift = 1 if shift1 else 2
        opposite_shift = 2 if shift1 else 1
        
        shifts[worker] = current_shift
        
        for neighbor in conflicts[worker]:
            if not is_valid(shifts, neighbor, current_shift):
                assign_shifts(neighbor, False)
    
    for worker in range(n):
        if shifts[worker] == 0:
            assign_shifts(worker, True)
            if any(not is_valid(shifts, w, None) for w in conflicts[worker]):
                stdout.write("NO\n")
                return
    
    stdout.write("YES\n")
    stdout.write(' '.join(map(str, shifts)) + '\n')

if __name__ == "__main__":
    main()