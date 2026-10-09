from collections import defaultdict
import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    return n, m, edges

def compute_pulse_magnitudes(s_u, s_v):
    """Compute M_{u->v} and M_{v->u}"""
    M_uv = (17 * (s_u ** 3) + 27 * (s_v ** 2)) % 64
    M_vu = (17 * (s_v ** 3) + 27 * (s_u ** 2)) % 64
    return M_uv, M_vu

def is_valid_pair(s_u, s_v):
    """Check if the pair of multipliers is valid (pulses are different)"""
    M_uv, M_vu = compute_pulse_magnitudes(s_u, s_v)
    return M_uv != M_vu

# Precompute valid pairs
valid_pairs = {}
for s_u in [1, 2, 3]:
    for s_v in [1, 2, 3]:
        valid_pairs[(s_u, s_v)] = is_valid_pair(s_u, s_v)

def check_configuration(n, edges, config):
    """Check if a configuration is valid"""
    for u, v in edges:
        if not valid_pairs[(config[u], config[v])]:
            return False
    return True

def get_next_signature(V_prev, s):
    """Calculate next signature value"""
    return 4 * V_prev + s

def solve():
    n, m, edges = read_input()
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Try all 3^n configurations in lexicographical order
    # We can think of this as a base-3 number from [1,1,...,1] to [3,3,...,3]
    # But we need the minimal signature, which corresponds to lexicographically
    # smallest tuple when treated as digits in base-4 (since we multiply by 4)
    
    # Generate configurations in order that minimizes signature
    # This is equivalent to generating in lexicographic order of the assignment
    
    # Since n <= 40, brute force is too expensive. We need a smarter approach.
    # Let's use backtracking with pruning based on the signature
    
    # But let's first check if it's even possible by checking constraints
    
    # For small n, we can do backtracking
    # For larger n, we might need graph coloring approach
    
    # Let's implement a backtracking solution that tries assignments in 
    # lexicographical order to ensure we get the minimal signature
    
    def backtrack(pos, current_config, current_signature):
        if pos == n:
            # Check if this configuration is valid
            if check_configuration(n, edges, current_config):
                return current_config[:]
            else:
                return None
        
        # Try each multiplier in order 1, 2, 3 to maintain lex order
        for mult in [1, 2, 3]:
            current_config[pos] = mult
            # Check if this assignment violates any existing edge constraint
            valid_so_far = True
            for u, v in edges:
                # Only check if both nodes are assigned
                if u < pos and v == pos:  # u is already assigned, v is current
                    if not valid_pairs[(current_config[u], mult)]:
                        valid_so_far = False
                        break
                elif v < pos and u == pos:  # v is already assigned, u is current
                    if not valid_pairs[(mult, current_config[v])]:
                        valid_so_far = False
                        break
            
            if valid_so_far:
                result = backtrack(pos + 1, current_config, get_next_signature(current_signature, mult))
                if result is not None:
                    return result
        
        current_config[pos] = 0  # Backtrack
        return None
    
    # Start backtracking
    config = [0] * n
    result = backtrack(0, config, 0)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, result)))

solve()