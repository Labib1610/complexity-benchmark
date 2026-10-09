# Problem B — Server Maintenance

Time limit: 2 s   Memory limit: 256 MB

## Description

A distributed database relies on **n** servers (numbered 1..n) and **m** bidirectional synchronization links. Each link connects two servers.

The network architecture enforces a strict role-based topology. Every server is hardware-configured as either a "Proposer" or an "Acceptor". Synchronization links can only physically operate between a Proposer and an Acceptor. The hardware prevents any links between two Proposers or between two Acceptors. The specific role of each server is not recorded in your manifest, but the network is guaranteed to have been built according to this rule.

You need to schedule maintenance. A group of servers is considered **fully disconnected** if no synchronization link exists between any two servers within the group.

Given a target size **k**, determine whether it is possible to select a fully disconnected group of exactly **k** servers. If it is possible, report one such group.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a synchronization link between server **u** and server **v**. No link is listed twice, and the network is guaranteed to follow the Proposer/Acceptor topology described above.

## Output

If a fully disconnected group of **k** servers exists, print `YES` on the first line, then on the second line print **k** distinct server numbers forming such a group, separated by spaces. Any group in which no two servers are linked is accepted.

If no such group exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```

## Note

In Example 1, servers 1 and 2 (which must share the same hardware role) have no link between them and form a valid group. In Example 3, the largest fully disconnected group contains only 2 servers, making a group of 3 impossible.
