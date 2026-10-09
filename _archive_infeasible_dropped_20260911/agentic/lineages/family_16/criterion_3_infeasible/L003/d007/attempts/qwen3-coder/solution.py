import sys
import threading

def main():
    import sys
    import threading

    def solve():
        j, T = map(int, sys.stdin.readline().split())
        teams = []
        for i in range(j):
            p1, p2 = map(int, sys.stdin.readline().split())
            teams.append((p1, p2))

        # Check JOB i: For each team, if p1 + p2 > T, then even if we ignore all
        # other constraints, this team alone cannot fit with ordering.
        for i in range(j):
            p1, p2 = teams[i]
            if p1 + p2 > T:
                print(f"JOB {i + 1}")
                return

        # If no JOB certificate, check LOAD certificates.
        # LOAD 1: Suspend team ordering, and non-overlapping in lane 2.
        # So we only need to fit all primary vehicles in lane 1.
        sum_p1 = sum(p1 for p1, _ in teams)
        if sum_p1 > T:
            print("LOAD 1")
            return

        # LOAD 2: Suspend team ordering, and non-overlapping in lane 1.
        # So we only need to fit all secondary vehicles in lane 2.
        sum_p2 = sum(p2 for _, p2 in teams)
        if sum_p2 > T:
            print("LOAD 2")
            return

    threading.Thread(target=solve).start()

main()