# Problem B — Reversible Garments

Time limit: 1 s   Memory limit: 256 MB

A fashion designer is creating a complex garment made of $n$ reversible fabric panels, numbered 1 to $n$. Each panel must be laid out in one of two orientations: matte side up (represented by 1) or glossy side up (represented by 2).

The assembly instructions specify $m$ seams. Each seam joins two specific panels together. To maintain the structural integrity and visual contrast of the stitching technique, any two panels connected by a seam must be laid out with opposite finishes facing up (one must be matte, the other glossy).

Your task is to determine if it is possible to orient all $n$ panels such that every seam constraint is satisfied. Because the automated cutting machine processes panels in numerical order, if multiple valid configurations exist, you must output the one whose sequence of orientations is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$) — the number of fabric panels and the number of seams, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ indicating that a seam connects panel $u$ and panel $v$.

## Output
If no valid orientation of the panels exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of panel orientations.

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