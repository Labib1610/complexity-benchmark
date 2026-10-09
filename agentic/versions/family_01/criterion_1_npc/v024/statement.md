# Problem A — Frequency Allocation

Time limit: 2 s   Memory limit: 256 MB

A regional communication network consists of $n$ broadcast towers. The regulatory commission has allocated exactly three distinct frequency bands, designated as 1, 2, and 3. Every tower must be configured to operate on exactly one of these three bands.

Due to geographical proximity, certain pairs of towers will experience critical signal interference if they transmit on the same frequency band. You are given a list of $m$ such pairs. Determine whether it is possible to assign a frequency band to each tower such that no two towers at risk of interference share the same band.

## Input
The first line contains two integers $n$ and $m$ — the number of broadcast towers and the number of interference-prone pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that tower $u$ and tower $v$ will interfere if assigned the same frequency band.

## Output
If no interference-free configuration exists, print a single line containing NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $f_1, f_2, \dots, f_n$ (each being 1, 2, or 3), where $f_i$ is the frequency band assigned to tower $i$. If multiple valid configurations exist, you may output any of them.

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
