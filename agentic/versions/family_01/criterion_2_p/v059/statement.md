# Network Frequency Configuration

Time limit: 1 s   Memory limit: 256 MB

An array of $n$ broadcast stations, numbered $1$ through $n$, must be configured to operate on one of two available frequency bands, labeled $1$ and $2$.

To prevent mutual degradation, certain station pairs are identified as mutually exclusive. If two stations in such a pair are set to the same frequency band, signal degradation occurs. Thus, for every specified pair, the two stations must be set to different frequency bands.

Determine whether a valid frequency selection $s_i \in \{1, 2\}$ exists for every station $i \in \{1, \dots, n\}$ that satisfies all exclusion constraints. If one or more valid configurations exist, output `YES` followed by the configuration $(s_1, s_2, \dots, s_n)$ that is lexicographically smallest. If no valid configuration exists, output `NO`.

A sequence $(s_1, \dots, s_n)$ is lexicographically smaller than $(t_1, \dots, t_n)$ if at the smallest index $k$ where $s_k \neq t_k$, we have $s_k < t_k$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$) — the number of broadcast stations and the number of exclusion constraints.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that station $u$ and station $v$ cannot share the same frequency band.

## Output
If no valid frequency configuration exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line, followed by a second line containing $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid configuration.

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
