# Signal Separation Protocols

**Time limit:** 2 s  
**Memory limit:** 256 MB  

An array of $n$ signal emitters, indexed from 1 to $n$, must each be configured with a specific frequency mode. The hardware supports exactly three frequency modes, represented by the integers 1, 2, and 3.

To prevent destructive interference, certain pairs of emitters must maintain a minimum frequency distance. You are given a list of $m$ such critical pairs. For every critical pair $(u, v)$, the assigned modes $f_u$ and $f_v$ must satisfy the separation condition $|f_u - f_v| \ge 1$. If this condition fails for any of the $m$ pairs, the array cannot operate safely.

Your objective is to determine whether there exists a complete mode configuration for all $n$ emitters that satisfies the separation condition for all $m$ critical pairs. The critical pairs interlock to form a rigid structural requirement, where configuring one emitter heavily restricts the available modes for others.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$), representing the number of emitters and the number of critical pairs.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating a critical pair of emitters that must satisfy the separation condition.

## Output
If no valid configuration exists, print `NO` on a single line.
If a valid configuration is possible, print `YES` on the first line. On the second line, output a sequence of $n$ integers $f_1, f_2, \dots, f_n$ (where each $f_i \in \{1, 2, 3\}$) indicating the frequency mode assigned to emitter $i$. Should multiple valid configurations exist, output the one that is lexicographically first (evaluating the mode choice for emitter 1 first, then emitter 2, and so on).

## Example 1
**Input:**
```
4 5
1 2
1 3
2 3
1 4
2 4
```
**Output:**
```
YES
1 2 3 3
```

## Example 2
**Input:**
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
**Output:**
```
NO
```