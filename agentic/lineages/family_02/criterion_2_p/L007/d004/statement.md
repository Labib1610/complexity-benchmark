# Problem B — Acoustic Levitation Arrays

Time limit: 1 s   Memory limit: 256 MB

## Description
An acoustic levitation chamber contains $n$ transducer arrays. Each array $i$ ($1 \le i \le n$) must be assigned a phase state $s_i \in \{0, 1\}$.

The chamber is subject to $m$ harmonic constraints. Each constraint is defined by two non-zero integers $l_1$ and $l_2$. 

For any non-zero integer $v$ such that $1 \le |v| \le n$, we define its *resonance index* $I(v)$ based on the phase state of array $|v|$:

$I(v) = v \cdot (2s_{|v|} - 1) + |v|$

To prevent destructive interference, a valid global assignment of phase states must ensure that for every harmonic constraint $(l_1, l_2)$, the sum of their resonance indices is strictly positive:

$I(l_1) + I(l_2) > 0$

Determine whether there exists a global assignment of phase states for all $n$ arrays that satisfies all $m$ harmonic constraints.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of transducer arrays and the number of harmonic constraints.
Each of the next $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($1 \le |l_1|, |l_2| \le n$), representing the parameters for a single constraint.

## Output
If no valid global assignment exists, print a single line NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) forming any valid assignment.

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
Multiple valid assignments may exist; any one is accepted. The same array index may appear in multiple constraints, and it is possible that $l_1 = l_2$ or $|l_1| = |l_2|$ within a single constraint.