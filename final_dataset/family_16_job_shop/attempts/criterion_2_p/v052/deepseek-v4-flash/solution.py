import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    cores = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        cores.append((p1, p2))
    
    # Johnson's rule
    first = []
    second = []
    for p1, p2 in cores:
        if p1 < p2:
            first.append((p1, p2))
        else:
            second.append((p1, p2))
    
    first.sort(key=lambda x: x[0])          # ascending by p1
    second.sort(key=lambda x: x[1], reverse=True)  # descending by p2
    
    order = first + second
    
    t_exc = 0
    t_damp = 0
    for p1, p2 in order:
        t_exc += p1
        if t_damp < t_exc:
            t_damp = t_exc
        t_damp += p2
    
    print(t_damp)

if __name__ == "__main__":
    main()