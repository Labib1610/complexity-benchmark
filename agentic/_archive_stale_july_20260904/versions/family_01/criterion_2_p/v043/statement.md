# Problem B — Harmonic Looms

Time limit: 1 s   Memory limit: 256 MB

The manufacturing plant operates $n$ mechanical looms. To prevent destructive harmonic resonance, each loom must be configured to run on exactly one of two timing cycles: cycle 1 or cycle 2.

The looms are connected by a network of $m$ rigid load-bearing struts. To cancel out vibrations, any two looms connected by a strut must operate in perfect opposition. This means that if one loom in the connected pair is set to cycle 1, the other must be set to cycle 2, and vice versa.

Your task is to determine whether it is possible to assign every loom to a timing cycle such that all strut constraints are satisfied. If multiple valid configurations exist, you must output the one that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$) — the number of looms and the number of struts.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of looms connected by a strut.

## Output
If no valid configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 \dots s_n$ (each either 1 or 2), representing the lexicographically smallest valid configuration.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
