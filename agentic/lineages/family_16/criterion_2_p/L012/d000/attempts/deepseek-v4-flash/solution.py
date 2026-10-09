import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    docs = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        docs.append((p1, p2))
    
    # Johnson's rule
    first = []
    second = []
    for p1, p2 in docs:
        if p1 <= p2:
            first.append((p1, p2))
        else:
            second.append((p1, p2))
    
    first.sort(key=lambda x: x[0])
    second.sort(key=lambda x: x[1], reverse=True)
    order = first + second
    
    t_translator = 0
    t_proofreader = 0
    for p1, p2 in order:
        t_translator += p1
        if t_proofreader < t_translator:
            t_proofreader = t_translator
        t_proofreader += p2
    
    print(t_proofreader)

if __name__ == "__main__":
    main()