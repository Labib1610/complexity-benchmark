import sys

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # For each emitter, store possible detectors
    detector_options = [[] for _ in range(k)]
    filter_of_emitter = [0] * k
    triplet_info = {}  # (emitter, detector) -> filter
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        z -= 1
        filter_of_emitter[x] = y
        detector_options[x].append(z)
        triplet_info[(x, z)] = y
    
    # Bipartite matching: emitters (0..k-1) to detectors (0..k-1)
    match_detector = [-1] * k  # which emitter is matched to detector
    
    def dfs(emitter, visited):
        for det in detector_options[emitter]:
            if not visited[det]:
                visited[det] = True
                if match_detector[det] == -1 or dfs(match_detector[det], visited):
                    match_detector[det] = emitter
                    return True
        return False
    
    for e in range(k):
        visited = [False] * k
        if not dfs(e, visited):
            print("NO")
            return
    
    # If we got here, all emitters matched
    print("YES")
    for det, emitter in enumerate(match_detector):
        filt = filter_of_emitter[emitter]
        print(f"{emitter+1} {filt+1} {det+1}")

if __name__ == "__main__":
    main()