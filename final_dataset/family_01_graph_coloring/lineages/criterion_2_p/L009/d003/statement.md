# Problem B — Factory Tuning

Time limit: 1 s   Memory limit: 256 MB

The factory requires each of its $n$ machines to be set to a power mode of either 1 or 2. There are $m$ interference links between specific pairs of machines. A legacy controller accepts a link only when the $2 \times 2$ matrix $\begin{pmatrix} x & 1 \\ 1 & y \end{pmatrix}$, where $x$ and $y$ are the modes of the two connected machines, is invertible and its inverse matrix consists entirely of integers. You must assign a power mode to every machine such that all $m$ links are accepted by the controller.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a linked pair of machines.

## Output
If no valid assignment of modes exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid assignment.

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