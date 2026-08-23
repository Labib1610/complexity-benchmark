# Problem A — Repeater Calibration

Time limit: 2 s   Memory limit: 256 MB

You are deploying a network of $n$ signal repeaters. Each repeater must be configured to operate on exactly one of three available frequency bands, which are designated by the numbers 1, 2, and 3. 

Because of their geographic proximity, certain specific repeaters have overlapping broadcast zones. If two repeaters with overlapping zones are configured to the identical frequency band, their signals will scramble and fail. You will be provided with a list of these overlaps. Each entry in the list identifies two repeaters that cannot share the same frequency band.

Determine if there is a way to configure every repeater such that no scrambling occurs. 

## Input
The first line of the input contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), representing the number of repeaters and the number of overlapping zones, respectively. The repeaters are numbered from 1 to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that repeater $u$ and repeater $v$ have an overlapping broadcast zone. No pair of repeaters will be listed more than once.

## Output
If it is impossible to configure the repeaters without scrambling, output a single line containing `NO`.
If a valid configuration exists, output `YES` on the first line. On the second line, output $n$ integers $c_1, c_2, \dots, c_n$, where each $c_i \in \{1, 2, 3\}$ represents the frequency band assigned to repeater $i$. If there are multiple valid configurations, you must output the one that is lexicographically smallest. (A sequence $A$ is lexicographically smaller than sequence $B$ if, at the first position where they differ, the value in $A$ is strictly less than the value in $B$).

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
