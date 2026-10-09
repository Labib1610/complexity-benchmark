# Problem B — Telemetry Bridge Initialization

Time limit: 2 s
Memory limit: 256 MB

## Description
During the initialization of a global telemetry bridge, you must establish communication channels between ground operations and satellites. The system comprises $q$ ground arrays, numbered $1$ through $q$, and $q$ orbital relays, numbered $q+1$ through $2q$.

A diagnostic scan has identified $t$ viable transmission links. Each viable link connects one specific ground array to one specific orbital relay. 

Your objective is to select a subset of these viable links to form a complete network allocation. A network allocation is only valid if every ground array and every orbital relay is included in exactly one selected link. If any array or relay is left without a link, the system suffers a coverage gap; if any is assigned to multiple links, signal interference occurs. 

Determine whether a valid network allocation can be formed from the scanned links, and if so, output the links to activate.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of ground arrays and the number of viable links.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating a viable link between ground array $a$ and orbital relay $b$.

## Output
If a valid network allocation can be found, print `YES` on the first line, followed by $q$ lines each containing the two nodes of a selected link. If no such allocation exists, print `NO`.

## Example

**Input**
```
3 4
1 4
2 5
2 6
3 6
```

**Output**
```
YES
1 4
2 5
3 6
```
