# Problem A — Assembly Tolerances

Time limit: 2 s   Memory limit: 256 MB

A specialized manufacturing facility produces a complex device comprising $n$ machined components. Prior to final assembly, every single component must be coated with one of three distinct chemical sealants. These sealants are identified by the numeric codes 1, 2, and 3.

Due to the extreme precision of the manufacturing tolerances, specific pairs of components will sit flush against each other within the assembled device. If any two interlocking components receive the exact same sealant, their identical chemical properties will trigger a cross-linking reaction. This reaction permanently fuses the components together, which ruins the internal mechanics of the device. To prevent this critical failure, any two components that interlock must never share the same sealant.

Given the total number of components and the comprehensive list of interlocking pairs, determine if a safe sealant assignment exists for the entire device.

## Input
The first line contains two integers $n$ and $m$ — the number of machined components and the number of interlocking pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) indicating that component $u$ and component $v$ interlock.

## Output
If it is impossible to assign sealants without causing a fusion reaction, print a single line containing `NO`.
If a safe assignment is possible, print `YES` on the first line. On the second line, print $n$ integers $s_1 s_2 \dots s_n$ (where each $s_i \in \{1, 2, 3\}$), with $s_i$ being the sealant code for component $i$. Among all safe assignments, output the lexicographically smallest sequence (compare $s_1$ first, then $s_2$, and so on).

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