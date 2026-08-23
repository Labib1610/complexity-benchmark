# Secure Relay Configuration

Time limit: 1 s   Memory limit: 256 MB

A telecommunications network consists of $n$ data relays, numbered 1 to $n$. To initialize the network, each relay must be assigned a base encryption key of either 1 or 2.

The network contains $m$ synchronization channels, each establishing a direct link between a specific pair of relays. For a channel to successfully authenticate its endpoints, the bitwise XOR of the encryption keys assigned to the two connected relays must evaluate to exactly 3.

You need to determine if there is a valid key assignment for all $n$ relays that successfully authenticates all $m$ channels. If a valid assignment exists, you must output it. In cases where multiple valid assignments satisfy all requirements, you must output the assignment that forms the lexicographically smallest sequence of keys.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the numbers of two relays connected by a synchronization channel.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (each being 1 or 2), representing the lexicographically smallest valid sequence of encryption keys.

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