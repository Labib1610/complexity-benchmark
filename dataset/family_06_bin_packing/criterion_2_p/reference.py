import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    total = 0
    for i in range(n):
        total += int(data[idx + i])

    # Material may be split arbitrarily, so containers can be filled completely
    # except possibly the last. Minimum containers = ceil(total / C).
    bins = (total + C - 1) // C
    print(bins)


main()
