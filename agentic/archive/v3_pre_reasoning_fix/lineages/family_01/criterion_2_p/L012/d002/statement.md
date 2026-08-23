# Problem B — Optical Filter Calibration

Time limit: 1 s   Memory limit: 256 MB

You are configuring the optical lenses for a testing array of $n$ laser emitters, numbered 1 to $n$. Each emitter must be fitted with a focal filter. You can choose a filter of power 1 or power 2.

The system is monitored by $m$ interference channels. Each channel cross-beams the light from a specific pair of emitters. To achieve perfect phase cancellation in a channel, the cross-sectional strength of the combined beam must be exactly 2. The combined cross-sectional strength is calculated as the product of the powers of the two filters involved in that channel.

Because the automated control system requires a deterministic setup, if there are multiple valid ways to choose the filter powers, you must select the configuration that is lexicographically smallest. (A configuration is represented as a sequence of $n$ integers, where the $i$-th integer is the filter power for emitter $i$. Sequence $A$ is lexicographically smaller than sequence $B$ if $A$ has a smaller value at the first position where they differ).

If the interference constraints are inherently contradictory and no valid configuration exists, your calibration routine must halt by rejecting the setup.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of emitters and the number of interference channels, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a pair of emitters cross-beamed in a channel.

## Output
If no valid configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers (each either 1 or 2)—the lexicographically smallest valid configuration for the emitters.

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