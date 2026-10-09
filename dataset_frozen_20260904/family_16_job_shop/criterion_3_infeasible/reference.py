import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); T = int(data[idx + 1]); idx += 2
    p1 = [0] * j
    p2 = [0] * j
    for i in range(j):
        p1[i] = int(data[idx]); p2[i] = int(data[idx + 1]); idx += 2

    # Certificate 1: a single job's two sequential operations already exceed T.
    for i in range(j):
        if p1[i] + p2[i] > T:
            print(f"JOB {i + 1}")
            return

    # Certificate 2: a machine's total serial load exceeds T.
    if sum(p1) > T:
        print("LOAD 1")
        return
    if sum(p2) > T:
        print("LOAD 2")
        return

    # Inputs for this criterion always satisfy one of the certificates; defensive fallback.
    print("LOAD 1")


main()
