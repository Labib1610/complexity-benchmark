# Problem A — Full-Coverage Cell Deployment for the Regional Drill

Time limit: 5 s
Memory limit: 256 MB

## Description
You are coordinating the security sweeps for a regional emergency readiness drill. The drill area is divided into $3q$ sectors, numbered $1$ through $3q$. Initially, all $3q$ sectors are designated as *unsecured*.

You are provided with a catalog of $t$ sweep protocols. You may choose a collection of these protocols to execute. Executing a protocol triggers the following system logic:
1. The protocol targets its three predefined sectors.
2. If any of those three sectors is already designated as *secured*, a system conflict occurs and the drill aborts.
3. Otherwise, the three sectors' designations are updated to *secured*.

Your goal is to authorize a collection of protocols such that, when executed sequentially, the system reaches a state where all $3q$ sectors are *secured* and no abort has occurred. Determine if such a collection exists, and if so, which protocols to authorize.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $3q$ is the total number of sectors and $t$ is the number of available sweep protocols.
Each of the next $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the three sectors targeted by one protocol.

## Output
If it is possible to secure all sectors without a conflict, print `YES` on the first line. Then, print $q$ lines, each containing the three sectors of an authorized protocol.
If no such collection of protocols exists, print `NO`.

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
