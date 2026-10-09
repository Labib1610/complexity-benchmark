# Problem A — Ecological Zone Allocation

Time limit: 2 s
Memory limit: 256 MB

A wildlife conservation center needs to relocate $n$ rescued specimens into exactly three distinct ecological zones, which are designated by the codes 1, 2, and 3. Certain specimens are antagonistic towards each other and will engage in conflicts if placed in the same zone. You are provided with a list of all antagonistic pairs.

Your task is to assign each of the $n$ specimens to one of the three zones such that no two antagonistic specimens share the same zone. If it is impossible to safely distribute all specimens under these conditions, you must report this.

To facilitate your analysis, the input data is guaranteed to satisfy the following structural properties:
- The absolute difference between the numerical identifiers of the two specimens in any antagonistic pair is strictly less than $n$.
- The sum of the numerical identifiers for any antagonistic pair is at most $2n$.

## Input
The first line of the input contains two integers $n$ and $m$ — the number of specimens and the number of antagonistic pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The specimens are identified by integers from 1 to $n$.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing an antagonistic pair of specimens that cannot be assigned to the same ecological zone.

## Output
If there is no valid allocation of specimens to the three zones, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $z_1, z_2, \dots, z_n$ (where each $z_i \in \{1, 2, 3\}$), representing the zone assigned to specimen $i$. If multiple valid allocations exist, you may output any of them.

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
