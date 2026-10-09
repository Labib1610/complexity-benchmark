# Problem A — Assembly Tolerances

Time limit: 2 s   Memory limit: 256 MB

A specialized manufacturing facility produces a complex device made of $n$ machined parts. Before final assembly, every single part must be treated with exactly one of three available chemical sealants. These sealants are designated as 1, 2, and 3.

Because of the precise tolerances required, certain pairs of parts interlock flush against each other in the final device. If two interlocking parts are treated with the exact same sealant, the identical chemical properties cause a cross-linking reaction that permanently fuses them together, ruining the device's internal mechanics. To prevent this, any two parts that interlock must be treated with strictly different sealants.

You are given the number of parts and the full list of interlocking pairs. Determine if it is possible to assign a sealant to every part without causing any interlocking pairs to fuse. 

## Input
The first line contains two integers $n$ and $m$ — the number of machined parts and the number of interlocking pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — an interlocking pair of parts.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $s_1 s_2 \dots s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the sealant applied to part $i$. Among all valid assignments output the lexicographically smallest sequence (compare $s_1$ first, then $s_2$, and so on).

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