# Rigid Structural Node

Time limit: 2 s   Memory limit: 256 MB

You are assembling a space frame from $n$ distinct structural struts, numbered 1 through $n$. The struts are connected using specialized joints. You are given a compatibility chart containing $m$ pairs of struts; each listed pair can be directly joined together.

To form a rigid structural node, you must select exactly three struts and join them together. This requires that all three struts are mutually compatible—meaning each strut in your selection can be directly joined to both of the other two struts in the selection.

Your task is to identify a valid set of three struts to form this rigid node. If multiple such sets exist, choose the set that is lexicographically first.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), the number of struts and the number of compatible pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of struts that can be joined.
It is guaranteed that at least one valid set of three struts exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, ordered such that $a < b < c$. These must represent three struts where the pairs $a$–$b$, $a$–$c$, and $b$–$c$ are all present in the compatibility chart. If there are multiple valid sets, output the one with the smallest $a$; in case of a tie, the smallest $b$; and then the smallest $c$.

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