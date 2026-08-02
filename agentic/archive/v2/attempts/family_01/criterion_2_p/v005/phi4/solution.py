from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    conflicts = [list(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(m)]
    
    workers_shift = [-1] * n
    
    def assign_shift(worker_id, shift):
        if workers_shift[worker_id] == -1:
            workers_shift[worker_id] = shift
        elif workers_shift[worker_id] != shift:
            print("NO")
            exit()
        
        for u, v in conflicts:
            if worker_id == u:
                assign_shift(v, 3 - shift)
            if worker_id == v:
                assign_shift(u, 3 - shift)
    
    for i in range(n):
        if workers_shift[i] == -1:
            assign_shift(i, 1)
    
    print("YES")
    print(' '.join(map(lambda x: str(x), workers_shift)))

if __name__ == "__main__":
    main()