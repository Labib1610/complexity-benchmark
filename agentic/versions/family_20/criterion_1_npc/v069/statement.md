# Problem A — Distributed Audit Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description
A distributed database cluster consists of servers and synchronization links. Each link connects exactly two servers. The cluster is designed so that every server is attached to exactly three synchronization links.

During the daily audit, every synchronization link must be activated exactly once. The audit is divided into three distinct network phases. A server's network interface can only handle one active synchronization link per phase. As a result, the three links connected to any given server must each be assigned to a different phase.

Assign every synchronization link to one of the three phases such that no server has more than one active link per phase. If it is impossible to schedule all links within the three phases under these conditions, report that it cannot be done.

## Input
The first line contains two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of servers and synchronization links, respectively.
Each of the following **m** lines contains two integers u and v (1 ≤ u < v ≤ n) indicating a synchronization link between server u and server v.

## Output
If a valid phase assignment exists, print `YES` on the first line. On the second line, print **m** integers from the set {1, 2, 3}, where the i-th integer represents the phase assigned to the i-th synchronization link in the input order. If no such assignment is possible, print `NO`.

## Example
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
YES
1 2 3 3 2 1
```
