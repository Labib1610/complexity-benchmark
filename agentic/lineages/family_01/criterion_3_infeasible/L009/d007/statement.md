# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The laboratory protocol requires isolating reactive materials to prevent hazards. Certain pairs of materials are documented as mutually volatile.

Your task is to identify a certificate of instability. A certificate consists of exactly three distinct materials. To determine if a given trio of materials is a certificate, we evaluate its internal reactivity. For each material in the trio, its internal reactivity score is defined as the number of other materials within that same trio with which it is mutually volatile. A trio forms a certificate of instability if and only if the product of the internal reactivity scores of its three materials is exactly 8.

It is guaranteed that the provided registry contains at least one such certificate.

## Input
The first line of the manifest contains two integers $n$ and $m$. The materials are assigned integer IDs from 1 to $n$. The facility requires at least 3 materials to conduct a trio analysis, and its containment vault can safely store up to 2000 materials, thereby setting the bounds for $n$.
Each of the subsequent $m$ lines contains two integers $u$ and $v$, representing a mutually volatile pair of materials. The number of documented pairs $m$ will be at least 3. The archive's maximum capacity is 200000 records, and $m$ will not exceed the maximum possible number of distinct pairs among the $n$ materials.
It is guaranteed that at least one certificate of instability exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$, representing the IDs of the materials that form a certificate. If there are multiple valid certificates, output the one that is lexicographically smallest (i.e., minimize $a$; in case of ties, minimize $b$; and if still tied, minimize $c$).

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