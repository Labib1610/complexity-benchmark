# Problem B — Linkage Configuration

Time limit: 1 s   Memory limit: 256 MB

You are designing a mechanical linkage with $n$ vertical sliders, identified by integers from 1 to $n$. Each slider $i$ is fixed at a horizontal coordinate $x = i$. Your task is to lock each slider at a vertical height $h_i$, which must be exactly 1 or 2.

The linkage contains $m$ rigid struts. Each strut connects slider $u$ and slider $v$. For the mechanism to assemble correctly without binding, the length of every strut must perfectly match its anchor points. Specifically, the Euclidean distance between the anchor point $(u, h_u)$ and the anchor point $(v, h_v)$ must be exactly $\sqrt{(u - v)^2 + 1}$. (If a slider is not connected to any struts, its height does not affect the assembly of other components).

Your task is to determine whether all sliders can be locked at valid heights such that every strut fits perfectly. If a valid configuration exists, you must provide the sequence of heights $h_1, h_2, \dots, h_n$ (where each $h_i \in \{1, 2\}$). If multiple valid sequences exist, you must output the one that produces the smallest possible value when evaluated as the sum $\sum_{i=1}^n h_i \cdot 3^{n-i}$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a strut connecting slider $u$ and slider $v$.

## Output
If there is no way to assign the heights without violating the strut length requirement, print a single line containing NO.
Otherwise, print YES on the first line. On the second line, print $n$ space-separated integers $h_1, h_2, \dots, h_n$ (each either 1 or 2), representing the valid configuration sequence that minimizes the required sum.

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