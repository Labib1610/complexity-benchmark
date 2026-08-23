# Secure Quorum Initialization

Time limit: 2 s
Memory limit: 256 MB

A distributed network consists of $n$ servers, assigned integer identifiers from $1$ to $n$. Through preliminary handshakes, $m$ specific pairs of servers have successfully exchanged symmetric cryptographic keys, allowing direct two-way communication between them.

To initialize a secure quorum, the system must select exactly three distinct servers. The initialization protocol requires absolute mutual trust among the chosen servers. This means that within the selected trio, every server must have successfully exchanged keys with both of the other two servers.

You are given the records of the $m$ successful key exchanges. It is guaranteed that at least one valid quorum of three servers can be formed. Your task is to determine the three servers for the quorum.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of servers and the number of key exchanges, respectively. The servers are assigned integer identifiers from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that server $u$ and server $v$ have exchanged keys.

It is guaranteed that at least one valid quorum of three servers can be selected.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the identifiers of the three servers. The identifiers must be printed in strictly increasing order ($a < b < c$).

If multiple such valid quorums exist, output the one that is lexicographically smallest (i.e., minimize $a$; in case of a tie, minimize $b$; and if still tied, minimize $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```