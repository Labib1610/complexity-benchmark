# Problem A — Legacy Server Migration

Time limit: 5 s
Memory limit: 256 MB

## Description
An IT department is decommissioning legacy servers. There are a total of $3q$ servers, identified by integers from $1$ to $3q$.

The automated migration software requires servers to be processed in pods of exactly three. Due to network topology constraints, only certain specific triples of servers can successfully communicate to form a valid pod. A list of $t$ compatible triples has been verified and provided by the engineering team.

The department must migrate every single server on the list. However, a server cannot be included in more than one migration pod, because running the protocol multiple times on the same machine corrupts its transit logs. 

You must determine if a valid selection of pods exists that migrates all servers perfectly without omissions or overlaps. If such a selection exists, you must also provide the list of pods to use.

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
Each of the next **t** lines contains three integers **a**, **b**, and **c** (1 ≤ a < b < c ≤ 3q), representing a compatible triple of servers.

## Output
If a valid selection exists, print `YES`, followed by **q** lines each containing the three server IDs of one chosen pod.
Otherwise, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
