# Problem C — Critical Hazard Report

Time limit: 2 s
Memory limit: 256 MB

A chemical storage facility handles $n$ compounds, numbered 1 through $n$. The safety system maintains a registry of $m$ reactive pairs; if two compounds form a reactive pair, they cannot be placed in the same storage room.

The facility operates with exactly two storage rooms, but an audit has determined the current inventory cannot be safely divided between them. To generate the mandatory incident report, the system must isolate a critical hazard: a group of exactly three distinct compounds where every compound in the group forms a reactive pair with the other two. Such a group inherently requires at least three storage rooms.

You must find and output the IDs of these three compounds. The IDs must be printed in increasing numerical order. If there are multiple critical hazards, you must output the lexicographically smallest group (the one with the smallest first ID; resolving ties with the smallest second ID, and further ties with the smallest third ID).

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a reactive pair of compounds. All reactive pairs are distinct.
It is guaranteed that at least one critical hazard exists.

## Output
Print three integers $a$, $b$, and $c$, separated by spaces, representing the IDs of the compounds in the critical hazard. Ensure that $a < b < c$.

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
