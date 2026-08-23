# Problem C — Triad Conflict Verification

Time limit: 2 s   Memory limit: 256 MB

A facility operates under strict assignment rules where certain pairs of workers cannot be assigned to the same operational shift. With $n$ workers numbered $1$ through $n$, the system contains $m$ recorded pairwise incompatibilities.

Analyzing all potential schedule configurations to prove that no valid two-shift assignment exists can involve inspecting many candidate combinations. However, any group of three distinct workers who are all mutually incompatible with one another provides a direct certificate of impossibility.

Your task is to identify one such group: a triple of worker IDs $(a, b, c)$ with $a < b < c$ such that all three pairs—$(a, b)$, $(a, c)$, and $(b, c)$—are explicitly listed as incompatible. Among all such valid triples, output the lexicographically smallest one (minimizing $a$, breaking ties by minimizing $b$, and then $c$).

It is guaranteed that at least one such mutually incompatible triple exists in the input.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ representing a pairwise incompatibility between worker $u$ and worker $v$.
It is guaranteed that at least one mutually incompatible triple exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are incompatible. Output the lexicographically smallest such triple.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
