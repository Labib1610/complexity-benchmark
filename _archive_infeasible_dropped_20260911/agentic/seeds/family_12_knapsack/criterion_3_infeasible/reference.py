import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); B = int(data[idx + 1]); idx += 2
    min_cost = None
    for _ in range(n):
        c = int(data[idx]); idx += 2   # value at data[idx+1] is unused for the certificate
        if min_cost is None or c < min_cost:
            min_cost = c

    # The cheapest investment costs min_cost > B, so no investment is affordable. Reporting
    # min_cost proves every cost exceeds the budget (B < min_cost <= every cost).
    print(f"MIN {min_cost}")


main()
