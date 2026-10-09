# Acoustic Resonance Tuning

Time limit: 1 s   Memory limit: 256 MB

A research facility operates $n$ sonic emitters. Each emitter must be configured to operate on one of two frequency bands, designated by the numeric values 1 and 2.

The facility contains $m$ interference zones. Each interference zone involves exactly two specific emitters. To prevent destructive resonance, the configuration must satisfy a strict safety condition: for any two emitters that share an interference zone, the sum of their assigned frequency band values must equal exactly 3.

You must determine if a safe configuration exists for all emitters. When multiple safe configurations exist, the facility's control system requires the sequence of $n$ frequency band assignments to be lexicographically smallest. That is, if two valid sequences differ, the preferred sequence is the one with the smaller value at the first position where they differ.

## Input
The first line of input provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of emitters and the number of interference zones. These bounds reflect the facility's maximum physical capacity.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), representing an interference zone between emitter $u$ and emitter $v$.

## Output
If no safe configuration can be found, output a single line containing `NO`.
If a safe configuration is possible, output `YES` on the first line. On the second line, output $n$ space-separated integers, where the $i$-th integer (either 1 or 2) represents the frequency band assigned to emitter $i$. This sequence must be the lexicographically smallest valid configuration.

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