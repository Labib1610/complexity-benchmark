# Problem A — Artificial Peptide Polymer

Time limit: 2 s   Memory limit: 256 MB

You are engineering an artificial peptide polymer composed of $n$ distinct subunits. Each subunit must be functionalized with exactly one of three available molecular markers, which are denoted by the integers 1, 2, and 3.

During the spatial conformation phase, certain pairs of subunits are brought into direct physical proximity. You are provided with a catalog of $m$ such proximity links. If two subunits connected by a proximity link are functionalized with the identical molecular marker, they will undergo an adverse reaction causing the polymer to experience structural collapse. Consequently, for every established proximity link, the two involved subunits must receive strictly distinct markers.

Due to the biophysical limitations of the polymer setup, the input is guaranteed to satisfy the following structural properties:
- The total number of proximity links $m$ across the entire polymer will never exceed 780.
- For any proximity link between subunit $u$ and subunit $v$, the product of their identifiers ($u \times v$) will not exceed 1600.

Your task is to determine whether there exists a safe marker functionalization for all $n$ subunits that prevents structural collapse.

## Input
The first line provides two integers $n$ and $m$ — the total number of subunits and the number of proximity links ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$, representing a proximity link between subunit $u$ and subunit $v$.

## Output
If no safe functionalization is possible, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the subsequent line, output $n$ integers $t_1, t_2, \dots, t_n$ (where each $t_i \in \{1, 2, 3\}$), representing the marker assigned to subunit $i$. If multiple safe functionalizations exist, you must output the one that is lexicographically smallest (i.e., compare the marker of subunit 1 first, then subunit 2, and so forth).

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
