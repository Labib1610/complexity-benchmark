import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    n = int(input_data[0])
    idx = 1
    S1 = []  # p1 <= p2, sort by p1 asc
    S2 = []  # p1 > p2, sort by p2 desc
    for _ in range(n):
        p1 = int(input_data[idx]); p2 = int(input_data[idx+1])
        idx += 2
        if p1 <= p2:
            S1.append((p1, p2))
        else:
            S2.append((p1, p2))
    S1.sort(key=lambda x: x[0])
    S2.sort(key=lambda x: x[1], reverse=True)
    order = S1 + S2
    prep_time = 0
    fin_time = 0
    for p1, p2 in order:
        prep_time += p1
        if prep_time > fin_time:
            fin_time = prep_time + p2
        else:
            fin_time += p2
    print(fin_time)

main()