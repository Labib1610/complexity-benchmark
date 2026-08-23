# Render Contrast

Time limit: 1 s
Memory limit: 256 MB

A visual synthesis engine is rendering a scene with $n$ material layers, numbered 1 through $n$. Each layer must be configured with a transparency mode, which takes an integer value of either 1 or 2.

The engine must enforce $m$ contrast constraints to prevent visual artifacts. Each constraint involves exactly two specific layers. To satisfy a constraint, the product of the transparency modes assigned to its two layers must evaluate to exactly 2.

Determine if there exists a valid configuration of transparency modes for all $n$ layers that satisfies every contrast constraint.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing two layers involved in a single contrast constraint.

## Output
If no valid configuration exists, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers representing the lexicographically smallest valid sequence of transparency modes for layers 1 through $n$.

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