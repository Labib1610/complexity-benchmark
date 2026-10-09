# Phase II: Channel Assignment

Time limit: 2 s   Memory limit: 256 MB

## Description
The deployment pipeline for the automated sensor network consists of three distinct phases. In Phase I, the environmental scanning service runs diagnostics on all endpoints to determine signal compatibilities, filtering out interference. This phase has now completed, handing off a list of $t$ viable communication links. 

You are responsible for Phase II: the channel assignment process. The network contains $2q$ endpoints in total. The first half of these, numbered $1$ through $q$, operate as primary broadcast nodes. The second half, numbered $q+1$ through $2q$, operate as secondary relay nodes. The Phase I diagnostics guarantee that every viable communication link pairs exactly one primary node with exactly one secondary node.

Your objective in Phase II is to select a subset of these viable links to form a complete network topology. The topology is considered complete if and only if every endpoint (all $2q$ of them) is utilized in exactly one selected link. If any endpoint is left without a link, or if an endpoint is assigned to multiple links, the topology is invalid and Phase III cannot proceed.

In Phase III, the firmware synthesis tool will compile the network topology. If you can successfully form a complete topology, you must pass the selected links to the synthesis tool. If no such topology can be formed from the Phase I data, you must halt the pipeline by reporting the failure.

## Input
The first line provides two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of primary nodes (with $2q$ being the total number of endpoints) and the number of viable links from Phase I.
Following this are $t$ lines, each containing two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$). Each line indicates a viable link between endpoint $a$ and endpoint $b$.

## Output
If a complete topology can be formed, print `YES` on the first line. Then, output $q$ lines, each containing the two endpoints of a selected link, to be passed to Phase III. If it is impossible to form a complete topology, print `NO`.

## Example

**Input**
```
3 5
1 4
1 5
2 5
3 5
3 6
```

**Output**
```
YES
1 4
2 5
3 6
```
