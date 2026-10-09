# Problem A — Phase Balancing in Homogeneous Topologies

Time limit: 5 s   Memory limit: 256 MB

## Description
A data center network consists of $n$ hubs and $m$ bidirectional links. The architecture is completely uniform: the number of links is exactly $1.5n$, and every hub terminates exactly the same number of links. This perfect regularity is designed to allow a completely balanced routing schedule.

The schedule operates in a cycle of distinct phases. To maximize throughput, the number of phases used in the network is exactly equal to the number of links attached to any single hub. To prevent buffer collisions, a hub cannot have two of its links active during the same phase. Because the number of phases matches the number of links per hub, this requirement is equivalent to saying every hub must have exactly one active link in every phase. 

Despite the uniform degree of every hub, the global wiring might still contain structural bottlenecks. Your task is to assign each link to exactly one of the available phases (numbered 1, 2, and 3) such that the collision-free property holds at every hub, or determine if the topology inherently prevents such a schedule.

## Input
The first line contains two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u < v \le n$), representing a link between hub $u$ and hub $v$.

## Output
If a valid phase assignment exists, print `YES`, followed by a line containing $m$ integers from the set $\{1, 2, 3\}$. The $i$-th integer specifies the phase for the $i$-th link in the input. If no such assignment is possible, print `NO`.

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
