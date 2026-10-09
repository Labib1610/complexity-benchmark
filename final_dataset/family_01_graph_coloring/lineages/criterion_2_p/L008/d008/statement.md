# Problem B — Anti-Glare Arrays

Time limit: 1 s
Memory limit: 256 MB

An optical instrument contains $n$ crystal lenses. Each lens must be assigned a polarization mode, which must be an integer value of either $1$ or $2$.

The instrument is equipped with $m$ calibration tubes, each routing data between a pair of lenses. The instrument's diagnostic system validates the configuration by checking the local resonance at each lens.

First, every calibration tube must be configured by designating one of its two endpoints as the 'anode' and the other as the 'cathode'. These endpoints inject resonance into their connected lenses. An anode endpoint injects $3$ units of resonance into its lens. A cathode endpoint injects $8$ units of resonance into its lens.

For each lens $i$, let $d_i$ be the total number of tube endpoints connected to it. (If a tube connects a lens to itself, it provides two endpoints to that lens. Because every tube has exactly one anode and one cathode, a self-loop naturally provides one anode endpoint and one cathode endpoint to its lens, contributing a combined $11$ units of resonance).

To successfully filter out glare, there must exist some valid configuration of all $m$ tubes such that for every lens $i$ (from $1$ to $n$), the total resonance injected into lens $i$ (the sum of resonance units from all tube endpoints connected to it) is exactly:
$d_i \cdot (5 c_i - 2)$
where $c_i$ is the assigned polarization mode of lens $i$.

Determine an assignment of polarization modes for all $n$ lenses that makes such a configuration possible, or report that the hardware configuration is flawed.

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