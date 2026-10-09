import sys

def main():
    data = sys.stdin.buffer.read().split()
    j = int(data[0])
    T = int(data[1])
    
    total_p1 = 0
    total_p2 = 0
    
    idx = 2
    for i in range(1, j + 1):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
        
        total_p1 += p1
        total_p2 += p2
    
    if total_p1 > T:
        print("LOAD 1")
    elif total_p2 > T:
        print("LOAD 2")

if __name__ == "__main__":
    main()