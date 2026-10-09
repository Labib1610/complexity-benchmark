import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    
    p1s = []
    p2s = []
    idx = 2
    for i in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        p1s.append(p1)
        p2s.append(p2)
        
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    if sum(p1s) > T:
        print("LOAD 1")
        return
    
    if sum(p2s) > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()