import sys

def main():
    data = sys.stdin.buffer.read().split()
    j = int(data[0])
    vessels = []
    idx = 1
    for _ in range(j):
        t1 = int(data[idx])
        t2 = int(data[idx + 1])
        idx += 2
        vessels.append((t1, t2))
    
    # Johnson's rule: sort by t1 ascending, t2 descending when t1 equal
    vessels.sort(key=lambda x: (x[0], -x[1]))
    
    alpha_end = 0
    beta_end = 0
    for t1, t2 in vessels:
        alpha_end += t1
        if beta_end < alpha_end:
            beta_end = alpha_end
        beta_end += t2
    
    print(beta_end)

if __name__ == "__main__":
    main()