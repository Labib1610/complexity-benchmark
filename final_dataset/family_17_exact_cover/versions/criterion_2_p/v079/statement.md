# Phase II: Channel Lock-in

Time limit: 2 s   Memory limit: 256 MB

## Description
The overall deployment protocol for the upcoming drill consists of three distinct phases. 

In Phase I (Environment Scanning), automated probes test the operational environment to identify stable synchronization channels. The deployment involves $2q$ distinct hardware modules. Modules with identifiers from $1$ to $q$ are emitters, while those with identifiers from $q+1$ to $2q$ are receivers. The probes generate a verified catalog of stable channels, where each channel connects exactly one emitter to one receiver. Unverified connections are strictly prohibited due to interference risks.

Your task is to execute Phase II (Channel Lock-in). You must process the catalog generated in Phase I and select a specific configuration of these channels. The configuration must utilize every single module (all emitters and all receivers, from $1$ to $2q$) exactly once. No module can be left idle, and no module can be assigned to more than one active channel. 

If you can successfully determine a valid configuration, Phase III (Drill Execution) will automatically commence, utilizing your selected channels for telemetry gathering. If no such configuration can be formed from the Phase I catalog, you must indicate that the drill cannot proceed.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a verified stable channel established during Phase I between emitter $a$ and receiver $b$.

## Output
If a Phase II lock-in configuration is possible, print `YES` followed by $q$ lines, each containing the two module identifiers of a selected channel. If no such configuration exists, print `NO`.

## Example

**Input:**
```
3 4
1 4
2 5
3 5
2 6
```

**Output:**
```
YES
1 4
3 5
2 6
```
