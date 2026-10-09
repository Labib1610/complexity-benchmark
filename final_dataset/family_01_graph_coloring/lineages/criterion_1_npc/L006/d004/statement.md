# Problem A — Harmonic Resonance

Time limit: 2 s
Memory limit: 256 MB

You are configuring a network of $n$ signal emitters. Each emitter must be assigned a base frequency multiplier, which must be exactly 1, 2, or 3.

The network is tested under $m$ interference conditions. Each condition involves a specific pair of emitters. When a pair of emitters $u$ and $v$ interact, they generate a resonance wave proportional to the product of their frequency multipliers, $c_u \times c_v$. 

To avoid destructive structural feedback, this product must never be the square of an integer (a perfect square). If $c_u \times c_v$ is a perfect square, the pair will cause a resonance failure.

Your task is to determine whether it is possible to assign a frequency multiplier $c_i \in \{1, 2, 3\}$ to every emitter $i$ (from $1$ to $n$) such that no resonance failures occur among the $m$ specified interacting pairs. If it is possible, provide a valid assignment.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of emitters and the number of interacting pairs.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing that emitter $u$ and emitter $v$ interact. It is guaranteed that each unordered pair $\{u, v\}$ appears at most once in the input.

## Output
If there is no valid assignment, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $c_1, c_2, \dots, c_n$, where each $c_i \in \{1, 2, 3\}$ is the frequency multiplier assigned to emitter $i$. If multiple valid assignments exist, you may output any of them.

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