import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    max_p1 = max_p2 = 0
    for idx in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        # local contradiction check
        if p1 + p2 > T:
            print(f"JOB {idx}")
            return
        if p1 > max_p1:
            max_p1 = p1
        if p2 > max_p2:
            max_p2 = p2

    # global contradiction check
    if max_p1 * j > T:
        print("LOAD 1")
    else:
        # problem guarantees one of the two subsystems is inconsistent
        print("LOAD 2")

if __name__ == "__main__":
    main()