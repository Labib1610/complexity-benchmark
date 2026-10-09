# Problem B — Harmonic Resonance

Time limit: 1 s   Memory limit: 256 MB

A facility operates $n$ resonance generators, with $m$ interference testing links established between specific pairs of generators. You must configure each generator $i$ by assigning it a state $s_i \in \{1, 2\}$. 

To maintain system stability, every interference testing link must be balanced. Specifically, for each link connecting generator $u$ and generator $v$, the sum of the squares of their assigned states must be exactly $5$ (that is, $s_u^2 + s_v^2 = 5$).

Determine if there is a valid configuration for all generators such that every link is balanced. 

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of generators connected by an interference testing link.

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each in $\{1,2\}$) representing the valid configuration. If there are multiple valid configurations, output the lexicographically smallest sequence $s_1, s_2, \ldots, s_n$. (Lexicographic order compares $s_1$, then $s_2$, etc.)

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