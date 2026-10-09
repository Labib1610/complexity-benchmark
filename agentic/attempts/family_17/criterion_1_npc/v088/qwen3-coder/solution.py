from collections import defaultdict
import sys

def main():
    import sys
    import threading
    sys.setrecursionlimit(1 << 25)
    
    def solver():
        q, t = map(int, sys.stdin.readline().split())
        configs = []
        for _ in range(t):
            a, b, c = map(int, sys.stdin.readline().split())
            configs.append((a, b, c))
        
        # This is essentially a exact cover problem.
        # We want to select exactly q triples such that each number from 1 to 3q appears exactly once.
        # We can model this as a graph matching or use backtracking with pruning.
        
        # Since q <= 200 and t <= 20000, and we need an exact cover,
        # we can try to model this as a matching problem or use DLX (Dancing Links) but that's overkill.
        # Let's use backtracking with optimization.
        
        # Build a graph: for each person, which triples contain them
        person_to_triples = defaultdict(list)
        for idx, (a, b, c) in enumerate(configs):
            person_to_triples[a].append(idx)
            person_to_triples[b].append(idx)
            person_to_triples[c].append(idx)
        
        # We need to select exactly q triples, covering all persons 1..3*q exactly once
        selected = [False] * t
        used_person = [False] * (3*q + 1)
        result = []
        
        def backtrack(triple_index):
            # If we've selected q triples, check if all persons are covered
            if len(result) == q:
                # Check if all persons are used
                for i in range(1, 3*q + 1):
                    if not used_person[i]:
                        return False
                return True
            
            # Pruning: if remaining triples can't cover remaining persons, return False
            # Not easily done, so let's just proceed
            
            # Try to pick next triple
            for i in range(triple_index, t):
                a, b, c = configs[i]
                if not selected[i] and not used_person[a] and not used_person[b] and not used_person[c]:
                    # Select this triple
                    selected[i] = True
                    used_person[a] = used_person[b] = used_person[c] = True
                    result.append(i)
                    
                    if backtrack(i + 1):
                        return True
                    
                    # Backtrack
                    selected[i] = False
                    used_person[a] = used_person[b] = used_person[c] = False
                    result.pop()
            
            return False
        
        # Optimization: sort triples by the minimum person number to try smaller ones first
        # This might help in pruning
        # Let's try without sorting first
        
        if backtrack(0):
            print("YES")
            for idx in result:
                a, b, c = configs[idx]
                print(a, b, c)
        else:
            print("NO")
    
    threading.Thread(target=solver).start()

if __name__ == "__main__":
    main()