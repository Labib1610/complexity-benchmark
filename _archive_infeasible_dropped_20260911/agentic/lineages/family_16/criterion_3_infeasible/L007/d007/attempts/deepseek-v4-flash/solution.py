import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    p1 = []
    p2 = []
    idx = 2
    for i in range(j):
        a = int(data[idx]); b = int(data[idx+1])
        idx += 2
        p1.append(a)
        p2.append(b)
        if a > T or b > T or a + b > T:
            print(f"JOB {i+1}")
            return

    # Check LOAD 1
    max1 = max(p1)
    # find second max
    second1 = 0
    count_max = 0
    for v in p1:
        if v == max1:
            count_max += 1
    if count_max >= 2:
        second1 = max1
    else:
        second1 = max(v for v in p1 if v != max1)
    if max1 + second1 > T:
        print("LOAD 1")
        return

    # Check LOAD 2
    max2 = max(p2)
    count_max2 = 0
    for v in p2:
        if v == max2:
            count_max2 += 1
    if count_max2 >= 2:
        second2 = max2
    else:
        second2 = max(v for v in p2 if v != max2)
    if max2 + second2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()