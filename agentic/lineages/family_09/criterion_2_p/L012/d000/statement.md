# Safe Cluster Deployment

Time limit: 2 s   Memory limit: 256 MB

## Description

You are deploying a distributed application across **n** servers (numbered 1 to **n**). There are **m** pairs of servers that share a vulnerable network channel. If both servers in such a pair are activated, they will cause a data collision.

The network was wired according to a strict alternating-tier protocol. It is guaranteed that there exists a way to assign each server a tier value of either 0 or 1, such that for every vulnerable channel connecting two servers, the sum of their tier values is exactly 1. (These tier values are internal and not provided to you).

A deployment cluster is considered **safe** if no two servers in the cluster share a vulnerable channel.

Given a target size **k**, determine whether a safe cluster of exactly **k** servers can be activated. If so, report one valid selection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 100000, 0 ≤ **m** ≤ 400000, 1 ≤ **k** ≤ **n**).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), representing a vulnerable channel between server **u** and server **v**. No channel is listed twice, and the network is guaranteed to follow the tier protocol described above.

## Output

If a safe cluster of **k** servers exists, print `YES` on the first line, then on the second line print **k** distinct server numbers forming such a cluster, separated by spaces. Any valid cluster without internal collisions is accepted.

If no such cluster exists, print `NO`.

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
