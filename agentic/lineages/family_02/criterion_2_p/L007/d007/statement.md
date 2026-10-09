# Problem B — Acoustic Levitation Arrays

Time limit: 1 s
Memory limit: 256 MB

## Description
An acoustic levitation chamber contains $n$ transducer arrays. Each array $i$ ($1 \le i \le n$) must be assigned a phase state $s_i \in \{0, 1\}$.

To prevent destructive interference, the chamber is equipped with $m$ acoustic interlocks. Each interlock monitors two arrays, specified by two non-zero integers $l_1$ and $l_2$. 

For each interlock, the effective interference $E$ is defined by the equation:
$$E = l_1 (2s_{|l_1|} - 1) + l_2 (2s_{|l_2|} - 1)$$

An interlock will trigger a system halt if the interference $E$ drops to or below a critical threshold $C$, which is defined for each interlock as:
$$C = -(|l_1| + |l_2|)$$

Therefore, a valid global configuration must ensure that for every interlock, the strict inequality $E > C$ holds.

Determine whether there exists a global assignment of phase states for all $n$ arrays that prevents any of the $m$ interlocks from triggering a halt.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of transducer arrays and the number of safety interlocks.
Each of the next $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($1 \le |l_1|, |l_2| \le n$), representing the parameters for a single interlock.

## Output
If no valid global assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) forming any valid assignment.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid assignments may exist; any one is accepted. The same array index may appear in multiple interlocks, and it is possible that $l_1 = l_2$ or $|l_1| = |l_2|$ within a single interlock.