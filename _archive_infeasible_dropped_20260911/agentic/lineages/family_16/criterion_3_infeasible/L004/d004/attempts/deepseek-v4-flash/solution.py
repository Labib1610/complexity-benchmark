import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    idx = 2
    p1_list = []
    p2_list = []
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        p1_list.append(p1)
        p2_list.append(p2)
        if p1 + p2 > T:
            print(f"JOB {_+1}")
            return

    sum1 = sum(p1_list)
    sum2 = sum(p2_list)
    if sum1 > T:
        print("LOAD 1")
    elif sum2 > T:
        print("LOAD 2")

if __name__ == "__main__":
    main()