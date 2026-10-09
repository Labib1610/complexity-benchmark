# Problem A — Data Center Fiber Link Maintenance

Time limit: 5 s   Memory limit: 256 MB

## Description
A tech company manages a core network topology where routing switches are connected by bidirectional fiber links. The topology is strictly homogeneous: every switch is an endpoint for exactly three fiber links.

During a major upgrade cycle, each fiber link must be taken offline for maintenance during exactly one of three available operational phases (labeled 1, 2, and 3). To prevent any switch from losing routing capability, no two links connected to the same switch can be taken offline during the same phase. The three links meeting at any switch must therefore be assigned to three distinct phases.

Furthermore, corporate policy dictates a strict global workload balance: exactly $n/2$ links must be assigned to each of the three phases (where $n$ is the total number of switches). 

Your task is to assign each link to one of the three phases such that both the local switch isolation rules and the global balancing requirements are satisfied, or determine that no such schedule is possible for the given network.

## Input
The first line contains two integers `n` and `m` (where `n` is even, `m = 3n/2`, and `2 ≤ n ≤ 2000`).
The following `m` lines each contain two integers `u` and `v` (`1 ≤ u < v ≤ n`), indicating a fiber link connecting switch `u` and switch `v`.

## Output
If a valid phase assignment exists, print `YES` on the first line. On the next line, print `m` integers from the set `{1, 2, 3}`, where the $i$-th integer represents the phase of the $i$-th link in the input order (links sharing a switch must have different phases). If no schedule can satisfy all requirements, print `NO`.

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
