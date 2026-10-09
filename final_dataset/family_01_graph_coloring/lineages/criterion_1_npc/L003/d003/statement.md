# Acoustic Levitation Arrays

Time limit: 2 s   Memory limit: 256 MB

You are tasked with tuning an acoustic levitation array consisting of $n$ wave emitters. The acoustic chamber is equipped with a maximum of 40 mounting slots, so the number of emitters will never exceed this capacity. For the system to function, every emitter must be assigned a phase offset. The hardware allows exactly three distinct offset modes, identified by the numeric codes 1, 2, and 3.

Due to the geometry of the system, certain pairs of emitters project sound waves that converge at shared focal points. In total, there are $m$ such pairs. When a pair of emitters targets the same focal point, their acoustic outputs interact. This interaction is modeled by a $2 \times 2$ interference matrix, where the first row contains the numeric codes assigned to the two emitters, and the second row contains the value 1 in both positions. 

If this matrix is singular (meaning its determinant is exactly zero), the waves resonate and the interference becomes perfectly constructive. This causes a localized pressure spike that destroys the levitated specimen. Therefore, for the system to operate safely, the interference matrix for the codes assigned to any two emitters that share a focal point must be invertible.

You must determine whether it is possible to assign a safe phase offset code to all $n$ emitters given the list of interacting pairs.

## Input
The first line contains two integers $n$ and $m$ — the number of emitters and the number of interacting emitter pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). Emitters are indexed from $1$ to $n$.
Each of the subsequent $m$ lines provides two integers $u$ and $v$ ($1 \le u, v \le n$), specifying that emitter $u$ and emitter $v$ share a focal point.

## Output
If a safe tuning is impossible, output a single line containing NO.
If a valid tuning exists, output YES on the first line. On the second line, output $n$ space-separated integers $p_1, p_2, \dots, p_n$ (where each $p_i \in \{1, 2, 3\}$), representing the offset code assigned to emitter $i$. Any valid array configuration will be accepted.

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