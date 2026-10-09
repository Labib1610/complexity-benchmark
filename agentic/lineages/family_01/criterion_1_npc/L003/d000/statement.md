# Acoustic Levitation Arrays

Time limit: 2 s   Memory limit: 256 MB

You are calibrating a set of $n$ acoustic levitation emitters. Each emitter must be configured to operate at a specific phase offset. The hardware supports exactly three phase offsets, which are represented by the configuration codes 1, 2, and 3.

The spatial arrangement of the array means that $m$ specific pairs of emitters have overlapping focal points. When two emitters share a focal point, their acoustic waves interact. If both emitters are configured with the exact same phase offset, their waves will perfectly synchronize, doubling the local pressure and shattering the levitated sample. To maintain safe and stable levitation, any two emitters that share a focal point must be assigned distinct phase offsets.

Given the list of emitter pairs that share a focal point, determine if there is a valid phase configuration for all $n$ emitters.

## Input
The first line contains two integers $n$ and $m$ — the number of emitters and the number of overlapping focal points ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that emitter $u$ and emitter $v$ share a focal point.

## Output
If no safe configuration exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $p_1, p_2, \dots, p_n$ (each in $\{1, 2, 3\}$), where $p_i$ is the phase configuration code for emitter $i$. If there are multiple valid configurations, any of them is accepted.

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
