# Problem B — Broadcast Configuration

Time limit: 1 s   Memory limit: 256 MB

A modernized communications grid consists of $n$ broadcast stations. Each station must be configured to use either the primary band (denoted by the integer 1) or the secondary band (denoted by the integer 2). 

However, there are $m$ specific pairs of stations that are situated too close to each other. If both stations in such a pair are configured to broadcast on the identical band, they will cause critical interference. 

You must find a band assignment for every station that completely avoids critical interference, or determine that no such assignment can be made.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of stations that will interfere if assigned the same band.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $f_1, f_2, \dots, f_n$ (each in $\{1, 2\}$), representing the band assigned to each station. If there are multiple valid assignments, output the sequence that is lexicographically smallest.

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
