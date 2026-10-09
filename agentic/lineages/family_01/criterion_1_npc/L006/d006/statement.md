# Problem A — Quantum Interference

Time limit: 2 s
Memory limit: 256 MB

You are tuning a network of $n$ quantum resonators. Each resonator must be assigned a discrete energy state, which must be exactly 1, 2, or 3.

The network is tested under $m$ coupling conditions. Each condition involves a specific pair of resonators. When a pair of resonators $u$ and $v$ are coupled, they generate an interference wave. The interference energy contributed by this coupled pair is determined by their assigned states $s_u$ and $s_v$, according to the following formula:
$$E(u, v) = 5(s_u - s_v)^4 - 25(s_u - s_v)^2 + 13$$

To avoid destructive feedback and achieve stable network resonance, the total interference energy of the system—defined as the sum of $E(u, v)$ over all $m$ coupled pairs—must be exactly equal to $-7m$.

Your task is to determine whether it is possible to assign an energy state $s_i \in \{1, 2, 3\}$ to every resonator $i$ (from $1$ to $n$) such that the total interference energy of the network is exactly $-7m$ among the $m$ specified coupled pairs. If it is possible, provide a valid assignment.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of resonators and the number of coupled pairs.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing that resonator $u$ and resonator $v$ are coupled. It is guaranteed that each unordered pair $\{u, v\}$ appears at most once in the input.

## Output
If there is no valid assignment, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$, where each $s_i \in \{1, 2, 3\}$ is the energy state assigned to resonator $i$. If multiple valid assignments exist, you may output any of them.

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