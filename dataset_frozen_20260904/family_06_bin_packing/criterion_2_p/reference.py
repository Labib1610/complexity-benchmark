import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    w = [int(data[idx + i]) for i in range(n)]; idx += n

    # Every item weighs more than C/3, so at most two fit in a container. Minimum containers by the
    # two-pointer greedy: pair the heaviest remaining with the lightest remaining if they fit,
    # otherwise the heaviest goes alone. This is optimal when no container holds more than two.
    order = sorted(range(n), key=lambda i: w[i])   # item indices sorted by weight ascending
    assign = [0] * n
    i, j = 0, n - 1
    bins = 0
    while i <= j:
        bins += 1
        if i == j:
            assign[order[i]] = bins
            break
        if w[order[i]] + w[order[j]] <= C:
            assign[order[i]] = bins
            assign[order[j]] = bins
            i += 1; j -= 1
        else:
            assign[order[j]] = bins
            j -= 1

    sys.stdout.write(f"{bins}\n")
    sys.stdout.write(" ".join(map(str, assign)) + "\n")


main()
