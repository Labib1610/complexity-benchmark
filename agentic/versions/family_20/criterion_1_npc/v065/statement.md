# Symmetric Channel Scheduling in Datacenters

Time limit: 5 s   Memory limit: 256 MB

## Description
A datacenter's communication fabric is built from $n$ modules and $m$ bidirectional channels. The architecture is strictly uniform: the total number of channels is exactly $1.5n$, and every module acts as an endpoint for exactly the same number of channels. 

To manage thermal load, the channels must be distributed across three distinct operational shifts (labeled 1, 2, and 3). Every channel must be assigned to exactly one shift. 

To ensure zero interference, no module can have two of its connected channels active during the same shift. Because of the network's uniform connectivity, this requires that every module has exactly one active channel in every shift.

You are guaranteed that all test inputs satisfy two structural properties:
1. The total number of channels $m$ is always a multiple of 3.
2. For any subset of $k$ modules, the number of channels completely internal to that subset (where both endpoints are in the subset) is at most $\lfloor 1.5k \rfloor$.

Your task is to determine a valid shift assignment for all $m$ channels such that the interference-free property holds at every module, or to detect if the topology makes such an assignment impossible.

## Input
The first line contains two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u < v \le n$), representing a bidirectional channel between module $u$ and module $v$.

## Output
If a valid shift assignment exists, print `YES` on the first line. On the second line, print $m$ integers from the set $\{1, 2, 3\}$, where the $i$-th integer is the shift assigned to the $i$-th channel in the input. If no such assignment is possible, print `NO`.

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
