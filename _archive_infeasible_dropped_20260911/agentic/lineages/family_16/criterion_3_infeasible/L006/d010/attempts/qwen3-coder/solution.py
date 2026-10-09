import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    p1 = [0] * j
    p2 = [0] * j
    
    index = 2
    for i in range(j):
        p1[i] = int(data[index])
        p2[i] = int(data[index+1])
        index += 2
    
    # Compute the normal final state to confirm SLA is violated
    u, v = 0, 0
    for i in range(j):
        u_new = u + p1[i]
        v_new = max(u_new + p2[i], v + p2[i])
        u, v = u_new, v_new
    
    # It's guaranteed that v > T
    # Now check which type of certificate to issue
    
    # Check Type A: Isolated
    # For each i, simulate applying only f_i and identity for others
    # We can compute prefix and suffix states efficiently
    
    # prefix_max_v[i] = max second coordinate when applying transformations 0 to i-1
    prefix_u = [0] * (j + 1)
    prefix_v = [0] * (j + 1)
    
    for i in range(j):
        u_prev = prefix_u[i]
        v_prev = prefix_v[i]
        u_new = u_prev + p1[i]
        v_new = max(u_new + p2[i], v_prev + p2[i])
        prefix_u[i+1] = u_new
        prefix_v[i+1] = v_new
    
    # suffix_u[i] = u coordinate after applying transformations from i to j-1, starting from (0,0)
    # suffix_v[i] = v coordinate after applying transformations from i to j-1, starting from (0,0)
    suffix_u = [0] * (j + 1)
    suffix_v = [0] * (j + 1)
    
    for i in range(j-1, -1, -1):
        # To compute suffix from i, we apply f_i to the suffix state from i+1
        # But we need to adjust for the prefix state
        # Actually, it's easier to think of it this way:
        # If we apply only f_i, the result is f_i applied to prefix state at i
        # Then we apply suffix transformation from i+1 starting from that result
        # But that's complex. Let's compute suffix_u and suffix_v as the transformation
        # that would be applied if we start from (0,0) at step i
        
        # Actually, let's recompute suffix properly:
        # suffix_u[i] and suffix_v[i] are the final (u,v) if we start at (0,0) and apply i to j-1
        # But we need the transformation that maps a state at step i to the final state
        # Let's instead compute the suffix transformation as a function
        # Let's think differently.
        
        # Let's compute for each i:
        # What is the final state if we apply f_i only and identity elsewhere?
        # That is: prefix_state[i] -> f_i -> then apply suffix from i+1
        # We need to compute the suffix transformation as a function that maps (u,v) to final (u,v)
        # Let's compute suffix transformation as (final_u_from_this_point, final_v_from_this_point)
        # But it's not a simple state, it's a transformation
        # The transformation from step i to end can be represented as:
        # Given state (u,v) at step i, final state is (u + sum_{k=i}^{j-1} p1[k], 
        #    max over path of v + sum of p2 increments)
        # Actually, the suffix transformation is more complex because of the max operations.
        
        # Let's compute suffix_u[i], suffix_v[i] as the final state if we start at (0,0) and apply from i to j-1
        # But that's not directly useful.
        
        # Let's compute for each i:
        # prefix state before i: (prefix_u[i], prefix_v[i])
        # Apply f_i: (prefix_u[i] + p1[i], max(prefix_u[i] + p1[i] + p2[i], prefix_v[i] + p2[i]))
        # Then apply suffix transformation from i+1
        # The suffix transformation from i+1 can be thought of as:
        # Given a state (u', v') at step i+1, what is the final state?
        # We can compute this by processing backwards.
        
        # Let's compute suffix transformation properly.
        # A transformation can be represented as a function f(u,v) = (u + du, max(v + dv, u + du + dv_offset))
        # But that's getting complex.
        
        # Simpler approach:
        # Compute all prefix states
        # Compute all suffix states
        # For each i, final state with only f_i is:
        #   start with prefix_state[i]
        #   apply f_i
        #   apply suffix transformation from i+1
        
        # Let's compute suffix transformation as a sequence
        # Or compute suffix_u_end[i], suffix_v_end[i] = final state if we start at (0,0) at step i
        
        # Let's try a different approach for suffix:
        # suffix_u_end[i] = final u if we start at (0,0) and apply from step i
        # suffix_v_end[i] = final v if we start at (0,0) and apply from step i
        pass
    
    # Let's compute suffix properly
    suffix_u_end = [0] * (j + 1)
    suffix_v_end = [0] * (j + 1)
    suffix_u_end[j] = 0
    suffix_v_end[j] = 0
    
    for i in range(j-1, -1, -1):
        u_prev = suffix_u_end[i+1]
        v_prev = suffix_v_end[i+1]
        # Apply transformation i starting from (0,0) to get to (u_prev, v_prev) conceptually
        # Actually, let's think of suffix_u_end[i] as the final u if we start applying from step i with initial (0,0)
        # No, let's think of suffix_u_end[i] as what the final state would be if we apply transformations i to j-1 starting from (0,0)
        u_new = 0 + p1[i]
        v_new = max(u_new + p2[i], 0 + p2[i])
        # But this is just applying one step. We need to compose.
        # Let's do it properly:
        # suffix from i means: apply f_i, then the suffix from i+1
        # If suffix from i+1 transforms (u',v') to (uf,vf), then
        # f_i transforms (u,v) to (u+p1[i], max(u+p1[i]+p2[i], v+p2[i]))
        # Then suffix from i+1 transforms that to final state
        # Let's represent suffix transformation as a function
        # For now, let's compute suffix_u_end and suffix_v_end as the state obtained by applying i..j-1 starting from (0,0)
        # This is not what we want for composition.
        
        # Let's restart the suffix computation:
        # suffix_u_end[i], suffix_v_end[i] = state at end if we apply i..j-1 starting from (0,0)
        suffix_u_end[i] = suffix_u_end[i+1] + p1[i]
        # For v, it's more complex due to max
        # suffix_v_end[i] = max(suffix_u_end[i] + p2[i], suffix_v_end[i+1] + p2[i])
        suffix_v_end[i] = max(suffix_u_end[i] + p2[i], suffix_v_end[i+1] + p2[i])
    
    # Now, for each i, to compute the state when only f_i is applied:
    # Start with (0,0)
    # Apply 0..i-1: reach (prefix_u[i], prefix_v[i])
    # Apply f_i: (prefix_u[i] + p1[i], max(prefix_u[i] + p1[i] + p2[i], prefix_v[i] + p2[i]))
    # Apply i+1..j-1 from this state
    # The effect of applying i+1..j-1 from state (u',v') is:
    # Final u = u' + (suffix_u_end[i+1] - 0) = u' + suffix_u_end[i+1]
    # Final v is more complex due to the max operations in the path
    # The suffix transformation is not just a shift.
    
    # Let's compute the suffix transformation as a function properly.
    # A state transformation can be represented as f(u,v) = (u + du, max(v + dv, u + offset))
    # But the composition is complex.
    
    # Let's take a simpler approach:
    # For Type A, for each i, compute the final state if we apply only f_i
    # We can do this by:
    # 1. Compute prefix state at i: (prefix_u[i], prefix_v[i])
    # 2. Apply f_i: (prefix_u[i] + p1[i], max(prefix_u[i] + p1[i] + p2[i], prefix_v[i] + p2[i]))
    # 3. Compute what the final state would be if we apply the suffix transformations from i+1
    #    starting from the state in step 2.
    # For that, we need to know the "effect" of the suffix transformations.
    
    # Let's compute for each position i, a "suffix transformation" that tells us
    # how the remaining steps affect a given state.
    # This is complex due to the max operations.
    
    # Alternative: simulate for each i the process with only f_i.
    # To do that efficiently, we can precompute:
    # - prefix_u[i], prefix_v[i]: state before step i
    # - suffix_u_from[i], suffix_v_from[i]: final state if we start applying from step i 
    #   with initial state (0,0)
    # But to compose, when we have state (u,v) at step i and want to apply suffix from i+1,
    # we need to know how the suffix affects (u,v).
    
    # The key insight is that the transformation f_k(u,v) = (u+p1, max(u+p1+p2, v+p2))
    # can be thought of in terms of how differences propagate.
    # But let's try a direct simulation approach for Type A first.
    
    # For Type A, let's compute for each i the final V if only step i is active.
    # The state before step i is (prefix_u[i], prefix_v[i])
    # After step i: (prefix_u[i] + p1[i], max(prefix_u[i] + p1[i] + p2[i], prefix_v[i] + p2[i]))
    # Then we need to apply steps i+1 to j-1.
    # The effect of steps i+1 to j-1 on a state (u', v') can be precomputed if we 
    # process backwards and represent the suffix transformation appropriately.
    
    # Let's represent a transformation as a function that maps (u,v) to (uf, vf)
    # For steps i to j-1, the transformation can be complex, but we can compute
    # for a given starting state what the final state is by processing forward.
    
    # Let's define suffix_transform[i] as a function that takes (u,v) and returns
    # the final state if we apply transformations i to j-1 starting from (u,v).
    # We can represent this transformation in a simplified way for our purposes.
    
    # Actually, let's compute suffix_final_u_if_start_with_u[i][u_val] but that's not feasible.
    
    # Let's think of the suffix transformation as:
    # Given state (u,v) at step i, the final state after applying i..j-1 is
    # (u + S1, max(v + S2, u + S3)) for some computed S1, S2, S3 that depend on p1[i..j-1], p2[i..j-1]
    # Let's see if this form is preserved.
    # f_i(u,v) = (u+p1[i], max(u+p1[i]+p2[i], v+p2[i]))
    # If we compose with a transformation g(ua,va) = (ua+S1, max(va+S2, ua+S3))
    # g(f_i(u,v)) = g(u+p1[i], max(u+p1[i]+p2[i], v+p2[i]))
    # = (u+p1[i]+S1, max(max(u+p1[i]+p2[i], v+p2[i]) + S2, u+p1[i]+S3))
    # = (u+(p1[i]+S1), max(u+p1[i]+p2[i]+S2, v+p2[i]+S2, u+p1[i]+S3))
    # = (u+(p1[i]+S1), max(v+p2[i]+S2, u+max(p1[i]+p2[i]+S2, p1[i]+S3)))
    # So if the suffix from i+1 is represented by S1', S2', S3', then
    # the suffix from i is represented by:
    # S1 = p1[i] + S1'
    # S2 = p2[i] + S2'
    # S3 = p1[i] + max(p2[i] + S2', S3')
    
    # Base case: suffix from j is identity: S1=0, S2=0, S3=-infty (since max(v+0, u-infty) = v)
    # But max(v+S2, u+S3) should be v, so S2 >= 0 and S3 <= S2 - "large"
    # Let's use S3 = S2 - 10^18 to simulate "ignore u"
    
    # Let's compute suffix parameters
    # suffix_params[i] = (S1, S2, S3) such that applying transformations i..j-1 to (u,v) gives
    # (u + S1, max(v + S2, u + S3))
    suffix_params = [(0, 0, -10**18)] * (j + 1)
    
    for i in range(j-1, -1, -1):
        S1_next, S2_next, S3_next = suffix_params[i+1]
        S1 = p1[i] + S1_next
        S2 = p2[i] + S2_next
        S3 = p1[i] + max(p2[i] + S2_next, S3_next)
        suffix_params[i] = (S1, S2, S3)
    
    # Now check Type A
    for i in range(j):
        # State before step i
        u_before = prefix_u[i]
        v_before = prefix_v[i]
        # Apply step i
        u_after = u_before + p1[i]
        v_after = max(u_after + p2[i], v_before + p2[i])
        # Apply suffix from i+1
        S1, S2, S3 = suffix_params[i+1]
        u_final = u_after + S1
        v_final = max(v_after + S2, u_after + S3)
        if v_final > T:
            print(f"JOB {i+1}")
            return
    
    # If Type A doesn't apply, then Type B must apply
    # Check Type B
    
    # Type B case c=1: use g_k(u, v) = (u + p_{1,k}, max(u + p_{1,k}, v))
    u, v = 0, 0
    for i in range(j):
        u_new = u + p1[i]
        v_new = max(u_new, v)
        u, v = u_new, v_new
    if v > T:
        print("LOAD 1")
        return
        
    # Type B case c=2: use h_k(u, v) = (u, max(u + p_{2,k}, v + p_{2,k}))
    u, v = 0, 0
    for i in range(j):
        u_new = u
        v_new = max(u + p2[i], v + p2[i])
        u, v = u_new, v_new
    if v > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()