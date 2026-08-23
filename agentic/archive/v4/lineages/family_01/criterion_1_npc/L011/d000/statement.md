# Problem A — Tri-Band Channel Assignment

Time limit: 2 s   Memory limit: 256 MB

A wireless network operates using three distinct frequency bands labeled 1, 2, and 3. There are $n$ transmitters in the network. Due to geographical proximity, certain pairs of transmitters interfere with one another and must not operate on the same frequency band. Assign every transmitter to exactly one frequency band so that no interfering pair shares a band, or report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of transmitters and the number of interfering pairs ($1 \le n \le 40, 0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an interfering pair of transmitters.

## Output
If no valid channel assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \ s_2 \ \dots \ s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the frequency band assigned to transmitter $i$. Among all valid assignments, output the lexicographically smallest sequence (comparing $s_1$ first, then $s_2$, and so on).

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
