# Problem C — Trust Quorum

Time limit: 2 s   Memory limit: 256 MB

You are auditing a decentralized security system that uses $n$ distinct cryptographic keys. The system has authenticated $m$ specific pairs of keys that can successfully undergo a mutual handshake protocol.

A "trust quorum" is established if exactly three distinct keys can all perform mutual handshakes with one another. The system logs guarantee that at least one such trust quorum has been formed. You must identify the keys involved.

## Input
The first line provides $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of cryptographic keys and the number of authenticated handshake pairs, respectively.
The following $m$ lines each contain two integers $u$ and $v$, indicating that key $u$ and key $v$ can perform a mutual handshake.
The input will always contain the handshakes necessary for at least one trust quorum involving three keys.

## Output
Output three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$. These must represent a trust quorum where the handshakes $a$–$b$, $a$–$c$, and $b$–$c$ are all present in the input. If there are multiple such quorums, provide the one that is lexicographically first (prioritizing the lowest value for $a$, then the lowest for $b$, and finally $c$).

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