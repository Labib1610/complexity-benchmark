# Problem B — Anti-Glare Arrays

Time limit: 1 s
Memory limit: 256 MB

An optical instrument contains $n$ crystal lenses. Each lens must be assigned a polarization mode, which must be an integer value of either $1$ or $2$.

The instrument is equipped with $m$ calibration tubes, each routing data between a pair of lenses. The instrument's diagnostic system validates the configuration by checking the local flow at each lens.

First, every calibration tube must be assigned a single direction of data flow (designating one of its lenses as the source and the other as the target). 

For each lens $i$, let $d_i$ be the total number of tube endpoints connected to it. (If a tube connects a lens to itself, it provides two endpoints to that lens). Based on the assigned directions, each endpoint at lens $i$ either brings data INTO lens $i$ (if $i$ is the target) or takes data OUT of lens $i$ (if $i$ is the source). A self-loop provides one incoming endpoint and one outgoing endpoint to its lens.

To successfully filter out glare, there must exist some valid assignment of directions to all $m$ tubes such that for every lens $i$ (from $1$ to $n$), the total number of endpoints bringing data INTO lens $i$ is exactly:
$d_i \cdot (c_i - 1)$
where $c_i$ is the assigned polarization mode of lens $i$.

Determine an assignment of polarization modes for all $n$ lenses that makes such a flow configuration possible, or report that the hardware configuration is flawed.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — the two lenses connected by that calibration tube.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES`, followed by a second line with $n$ integers $c_1 \dots c_n$ (each in $\{1,2\}$). This sequence must represent the valid calibration assignment. If multiple valid assignments exist, output the lexicographically smallest sequence.

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