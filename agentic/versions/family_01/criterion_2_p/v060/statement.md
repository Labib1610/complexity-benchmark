# Problem B — Orbital Bandwidth Allocation

Time limit: 1 s   Memory limit: 256 MB

An orbital network consists of $n$ communication satellites, numbered 1 through $n$. During initial deployment, technicians observed that certain pairs of satellites are positioned such that their signal footprints overlap. Specifically, there are $m$ known pairs of satellites that will cause destructive interference if they operate on the same frequency band.

Each satellite must be configured to broadcast permanently on one of two available frequency bands, designated as Band 1 and Band 2. A band configuration is represented as a sequence of $n$ integers, where the $i$-th integer specifies the band assigned to satellite $i$. A configuration is considered safe if, for every overlapping pair identified by the technicians, the two satellites in the pair are assigned to different frequency bands.

Your task is to analyze the overlap data and determine whether a safe configuration is possible for all $n$ satellites. If it is possible, you must find the safe configuration that is lexicographically smallest. If no safe configuration can be established, you must report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$, representing a pair of satellites whose signal footprints overlap.

## Output
If no safe configuration exists, print a single line containing the word NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $b_1 \dots b_n$ (each either 1 or 2), representing the lexicographically smallest safe configuration.

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
