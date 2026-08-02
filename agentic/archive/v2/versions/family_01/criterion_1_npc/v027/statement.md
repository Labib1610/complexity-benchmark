# Frequency Allocation Protocol

Time limit: 2 s   Memory limit: 256 MB

A wireless network consists of $n$ transmitters, indexed 1 through $n$. Certain pairs of transmitters generate cross-channel interference when operating simultaneously. To maintain signal integrity, any two transmitters that interfere with each other must operate on distinct frequency channels. The equipment supports three discrete frequency channels, identified by the numbers 1, 2, and 3. Each transmitter must be assigned to exactly one channel.

Determine if there exists a valid allocation of frequency channels to all transmitters that resolves all mutual interference restrictions. If no valid allocation exists, report that it is impossible. If one or more valid allocations exist, determine the allocation that produces the lexicographically smallest sequence of channel identifiers $s_1, s_2, \dots, s_n$, where $s_i$ denotes the channel assigned to transmitter $i$.

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of transmitters and the number of interfering pairs, respectively.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that transmitter $u$ and transmitter $v$ interfere with each other. No interfering pair is listed more than once.

## Output
If no valid allocation exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ is the channel assigned to transmitter $i$. This sequence must be the lexicographically smallest among all valid channel allocations (that is, comparing $s_1$ first, then $s_2$, and so forth).

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
