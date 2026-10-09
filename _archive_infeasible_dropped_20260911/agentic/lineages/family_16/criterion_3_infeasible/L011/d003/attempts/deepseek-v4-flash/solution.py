import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    idx = 2
    uplink_total = 0
    downlink_total = 0
    
    for i in range(1, j + 1):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
        uplink_total += p1
        downlink_total += p2
    
    if uplink_total > T:
        print("LOAD 1")
    elif downlink_total > T:
        print("LOAD 2")

if __name__ == "__main__":
    main()