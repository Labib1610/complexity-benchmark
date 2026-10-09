import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    
    total1 = 0
    total2 = 0
    
    for i in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
        total1 += p1
        total2 += p2
    
    if total1 > T:
        print("LOAD 1")
    elif total2 > T:
        print("LOAD 2")

if __name__ == "__main__":
    main()