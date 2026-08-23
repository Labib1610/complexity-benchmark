# Problem C — Rigid Cellular Structure

Time limit: 2 s
Memory limit: 256 MB

You are analyzing the blueprint of a large-scale structural framework. The framework consists of $n$ anchor points and $m$ straight steel struts. Each strut provides a bidirectional rigid connection between two distinct anchor points.

To ensure structural stability, the engineers rely on "fundamental rigid cells." A fundamental rigid cell is formed by exactly three distinct anchor points that are fully braced. This means that if a cell consists of anchor points $a$, $b$, and $c$, there must be a direct strut between $a$ and $b$, a direct strut between $a$ and $c$, and a direct strut between $b$ and $c$.

Your task is to locate one such fundamental rigid cell. The blueprint is extensive, but the engineering specifications guarantee that the current design contains at least one such cell.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of anchor points and the number of struts. Anchor points are designated by integers from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that a strut connects anchor point $u$ and anchor point $v$. It is guaranteed that there is at most one strut connecting any specific pair of anchor points, and that the framework contains at least one fundamental rigid cell.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the anchor points that make up the cell. You must list them in ascending order ($a < b < c$).

If there are multiple valid cells, output the one that is lexicographically smallest. A cell $(a_1, b_1, c_1)$ is lexicographically smaller than $(a_2, b_2, c_2)$ if $a_1 < a_2$; or if $a_1 = a_2$ and $b_1 < b_2$; or if $a_1 = a_2$, $b_1 = b_2$, and $c_1 < c_2$.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
