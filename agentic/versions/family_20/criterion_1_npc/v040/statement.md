# Problem A — Diagnostic Phase Assignment

Time limit: 5 s   Memory limit: 256 MB

## Description
The network engineering department is preparing a comprehensive latency report for a newly deployed data center. This process occurs in three stages.

First, an automated discovery tool maps all physical point-to-point connections between the hardware endpoints. The architecture is strictly uniform: the discovery tool guarantees that every endpoint terminates exactly a trio of connections. No endpoint has more or fewer.

Second, you must generate a schedule for the diagnostic tests. The testing suite operates in exactly three distinct phases (designated 1, 2, and 3). Each connection must be assigned to exactly one of these phases. To ensure accurate latency measurements, the hardware at any endpoint cannot process multiple connections simultaneously during the same phase. Thus, connections that share an endpoint must be assigned different phases. Because every endpoint terminates exactly three connections, a valid schedule requires that at every endpoint, its three incident connections are perfectly partitioned across the three phases.

Third, once your schedule is submitted, the testing suite will execute the phases sequentially and aggregate the latency metrics into the final report.

Your task is strictly to handle the second stage. Given the topology mapped by the discovery tool, determine if a valid phase assignment exists. If a schedule cannot be formed without causing a phase collision at some endpoint, you must report that it is impossible.

## Input
The first line contains two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000).
Each of the next **m** lines contains two integers u and v (1 ≤ u < v ≤ n), representing a connection between endpoint u and endpoint v.

## Output
If a valid phase assignment exists, print `YES`, followed by a line with **m** integers in {1, 2, 3} — the phase assigned to connection i in input order. Otherwise, print `NO`.

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
