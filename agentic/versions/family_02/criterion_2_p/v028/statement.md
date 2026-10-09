# Problem B — Ecological Safeguards

Time limit: 1 s   Memory limit: 256 MB

## Description

A botanical research facility houses $n$ distinct plant species. For optimal growth, each species must be cultivated in exactly one of two climate settings: Humid (represented by 1) or Arid (represented by 0).

The facility's ecologists have established $m$ survival criteria to ensure the artificial ecosystem remains stable. Each criterion highlights two specific climate states across the facility. A climate state is described by a non-zero integer $v$: if $v > 0$, it means species $v$ is placed in the Humid setting; if $v < 0$, it means species $|v|$ is placed in the Arid setting.

To prevent an ecological collapse, every survival criterion demands that at least one of its two listed climate states is actively maintained. 

Determine whether it is possible to assign a climate setting to each of the $n$ species such that all $m$ survival criteria are simultaneously fulfilled. If a valid configuration exists, provide one; otherwise, declare that no such arrangement is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of species and the number of survival criteria.
Each of the next $m$ lines contains two non-zero signed integers $l_1$ and $l_2$, with $|l_i| \le n$. At least one of the two stated climate states must hold for the criterion to be satisfied.

## Output
If no valid climate configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) forming any valid configuration, where $s_i$ represents the climate setting of species $i$.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid configurations may exist; any one is accepted. The same species or climate state may appear in multiple survival criteria.
