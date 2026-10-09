# Problem A — Phase Shift Configuration

Time limit: 2 s   Memory limit: 256 MB

A regional communication network consists of $n$ broadcast stations. Each station must be configured with a phase shift setting chosen from the options 1, 2, and 3.

The region contains $m$ overlapping coverage zones. Each zone is formed by the signals of two specific stations. If both stations forming a zone are configured with the identical phase shift setting, their signals will cancel out, rendering the zone inactive.

You are provided with the stations associated with each of the $m$ zones. Determine if it is possible to assign a phase shift setting to all $n$ stations such that no coverage zone is rendered inactive.

## Input
The first line contains two integers $n$ and $m$ — the number of broadcast stations and the number of overlapping coverage zones ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that station $u$ and station $v$ form a coverage zone.

## Output
If no valid configuration exists, print a single line containing NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $p_1, p_2, \dots, p_n$ (each being 1, 2, or 3), where $p_i$ is the phase shift setting assigned to station $i$. If multiple valid configurations exist, you may output any of them.

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
