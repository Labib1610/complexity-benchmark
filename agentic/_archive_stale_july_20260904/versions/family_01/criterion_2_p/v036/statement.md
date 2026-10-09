# Problem B — Broadcast Frequencies

Time limit: 1 s   Memory limit: 256 MB

A regional emergency broadcast system consists of $n$ radio transmitters. Each transmitter must be tuned to either the primary frequency (denoted as 1) or the secondary frequency (denoted as 2). Due to geographic proximity, $m$ specific pairs of transmitters will severely interfere with each other if they broadcast on the exact same frequency.

Your task is to determine if there is a way to tune all transmitters such that no interfering pair shares the same frequency. If such a tuning is impossible, you must report this. If multiple valid tunings exist, you must output the one that prioritises the primary frequency for the lowest-numbered transmitters. Specifically, the sequence of frequency assignments (from transmitter 1 to $n$) must be the smallest possible when compared element by element from left to right.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ $n$ ≤ 2·10⁵, 0 ≤ $m$ ≤ 2·10⁵), representing the number of transmitters and the number of interfering pairs, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that transmitters $u$ and $v$ will interfere if they share a frequency.

## Output
If there is no way to tune the transmitters without interference, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, \dots, s_n$ (where each $s_i \in \{1, 2\}$) representing the frequency assigned to each transmitter in the required optimal tuning.

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
