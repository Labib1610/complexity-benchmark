# Problem A — Oscillator Tuning

Time limit: 2 s   Memory limit: 256 MB

A control system consists of $n$ precision oscillators, numbered $1$ through $n$. Each oscillator requires a frequency multiplier to operate correctly. You must assign each oscillator a multiplier chosen from the set $\{1, 2, 3\}$.

Within the system, certain pairs of oscillators are connected by coupling links. When oscillator $u$ and oscillator $v$ are linked, their interaction generates a continuous bidirectional pulse. The magnitude of the forward pulse from oscillator $u$ to oscillator $v$ is given by $M_{u \to v} = s_u \cdot v + s_v \cdot u$, where $u$ and $v$ are the integer identifiers of the oscillators, and $s_u$ and $s_v$ are their assigned multipliers. Similarly, the magnitude of the reverse pulse from oscillator $v$ to oscillator $u$ is $M_{v \to u} = s_v \cdot v + s_u \cdot u$. 

To ensure system stability, these two pulse magnitudes must be strictly unequal ($M_{u \to v} \neq M_{v \to u}$). If any linked pair produces identical forward and reverse pulse magnitudes, the link undergoes resonance collapse and the entire system fails.

You must determine whether a stable configuration of multipliers exists for the given system.

## Input
The first line provides two integers $n$ and $m$ — the total number of oscillators and the number of coupling links ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), signifying that oscillator $u$ and oscillator $v$ are linked. It is guaranteed that each unordered pair of linked oscillators appears at most once in the input.

## Output
If there is no way to configure the multipliers without inducing resonance collapse, output a single line containing `NO`.
If a stable configuration is achievable, output `YES` on the first line. On the second line, provide $n$ integers $s_1 s_2 \dots s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ represents the multiplier assigned to oscillator $i$. 

If multiple stable configurations exist, you must output the one that minimizes the final system signature $V_n$. This signature is computed sequentially: starting with an initial value $V_0 = 0$, for each oscillator $i$ from $1$ to $n$ in order, the signature updates according to the rule $V_i = 4 \cdot V_{i-1} + s_i$.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```