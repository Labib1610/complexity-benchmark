import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))

    # We will store modules grouped by frequency.
    # For each frequency, we keep a list of (amplitude, phase).
    freq_groups = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        freq_groups[x].append((y, z))

    # We need to select exactly k modules, one per frequency (since frequencies must be distinct and there are k possible values).
    # This is a matching problem: assign each frequency a distinct amplitude and phase.

    # Since k <= 22, we can use DP over subsets of amplitudes and phases.

    # State: (mask_amp, mask_phase) -> possible? We'll do iterative DP over frequencies.
”
    # dp[mask_amp][mask_phase] = True if we can assign first f frequencies.

    # We'll store parent to reconstruct solution.

    # Number of states: 2^k * 2^k =  ～ 4^22 ≈  ～ 17 million, too large for memory if full.
    # But we can use dictionary for reachable states, and k <= 22, t <= k^3 =  ～ 10648.
    # In practice reachable states may be limited. We'll use dict of bitmask -> parent info.

    # We'll process frequencies one by one.
”
    # dp: dict mapping (amp_mask, phase_mask) -> (prev_amp_mask, prev_phase_mask, chosen_amp, chosen_phase)
    # Actually we can store for each state the previous state and chosen module.
”
    dp = {}
    dp[(0, 0)] = None  # (prev_state, chosen_amp, chosen_phase) or None for start

    for f in range(1, k + 1):
        if not freq_groups[f]:
            # No module for this frequency, impossible to select one per frequency.
”
            print("NO")
            return
        new_dp = {}
        # For each current state, try each module in this frequency group.

        for (amp_mask, phase_mask), prev_info in dp.items():
            for (a, p) in freq_groups[f]:
                if (amp_mask >> (a-1)) & 1:
                    continue
                if (phase_mask >> (p-1)) & 1:
                    continue
                new_amp_mask = amp_mask | (1 << (a-1))
                new_phase_mask = phase_mask |(1 << (p-1))
                if (new_amp_mask, new_phase_mask) not in new_dp:
                    new_dp[(new_amp_mask, new_phase_mask)] = (amp_mask, phase_mask, a, p)
        dp = new_dp
        if not dp:

            print("NO")
            return

    # After processing all k frequencies, we need a state with all amplitudes and phases used.
”
    full_mask = (1 << k) - 1
    if (full_mask, full_mask) not in dp:

        print("NO")
        return

    # Reconstruct solution.
”
    state = (full_mask, full_mask)
    chosen = []
    # We need to know which frequency each step corresponds to. We processed frequencies 1..k in order.
”
    # We'll reconstruct backwards: from final state, follow prev_info.
”
    # But we need to know frequency index. We can store frequency in prev_info as well.

    # Let's redo with storing frequency in prev_info. Easier: store in dp value: (prev_amp_mask, prev_phase_mask, freq, amp, phase)
”
    # We'll redo the DP with that info. Since k small, we can just re-run and store freq.

    dp = {}
    dp[(0, 0)] = None
    for f in range(1, k + 1):
        new_dp = {}
        for (amp_mask, phase_mask), prev_info in dp.items():
            for (a, p) in freq_groups[f]:
                if (amp_mask >> (a-1)) & 1:
                    continue
                if (phase_mask >> (p-1)) & 1:
                    continue
                new_amp_mask = amp_mask |(1 << (a-1))
                new_phase_mask = phase_mask |(1 << (p-1))
                if (new_amp_mask, new_phase_mask) not in new_dp:

                    new_dp[(new_amp_mask, new_phase_mask)] = (amp_mask, phase_mask, f, a, p)
        dp = new_dp
        if not dp:

            print("NO")
            return

    if (full_mask, full_mask) not in dp:

        print("NO")
        return

    # Reconstruct
    state = (full_mask, full_mask)
    while state != (0, 0):
        prev_amp_mask, prev_phase_mask, f, a, p = dp[state]
        chosen.append((f, a, p))
        state = (prev_amp_mask, prev_phase_mask)

    chosen.reverse()
    out = ["YES"]
    for f, a, p in chosen:
        out.append(f"{f} {a} {p}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()