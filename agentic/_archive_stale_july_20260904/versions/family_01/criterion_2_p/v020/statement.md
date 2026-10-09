# Magnetic Containment Field

Time limit: 1 s
Memory limit: 256 MB

You are programming the assembly sequence for a new fusion reactor's magnetic containment field. The field relies on $n$ electromagnetic emitters, numbered 1 through $n$. Each emitter must be calibrated to one of two phase states, designated as 1 and 2.

The reactor design specifies $m$ interference channels. Each channel connects a specific pair of emitters. If the two emitters connected by an interference channel are calibrated to the same phase state, their waves will resonate and destabilise the field. Therefore, they must always be calibrated to different phase states.

Determine if there is a valid calibration for all $n$ emitters that avoids destabilising the field. If multiple valid calibrations exist, the reactor's diagnostic system requires the one that is lexicographically smallest when the phase states of emitters 1 through $n$ are written as a sequence.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an interference channel between emitter $u$ and emitter $v$.

## Output
If no safe calibration exists, print a single line `NO`.
Otherwise print `YES`, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1, 2\}$), representing the lexicographically smallest valid calibration sequence.

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
