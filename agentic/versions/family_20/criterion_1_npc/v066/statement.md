# Problem A — Automated Phase Allocation for Network Upgrades

Time limit: 5 s
Memory limit: 256 MB

## Description
Our infrastructure management system executes a three-stage pipeline to upgrade regional data grids. You are responsible for implementing the middle stage: the scheduling module.

**Stage 1: Topology Discovery.** Automated tracers map the grid and output a list of endpoints and the physical conduits connecting them. The grids are built to a strict redundancy standard: every endpoint is the termination of exactly three conduits. This raw connectivity data is passed to your module.

**Stage 2: Operational Scheduling (Your task).** The upgrade requires taking conduits offline. The entire operation is divided into three distinct time periods. You must assign each conduit to period 1, period 2, or period 3. The critical safety invariant dictates that no endpoint may have more than one of its connected conduits offline during the same period. Because there are exactly three periods and exactly three conduits per endpoint, this invariant forces every endpoint to have its three conduits assigned to three different periods. If a valid schedule exists, your module must generate it. If the topology makes this impossible, your module must report the failure so the upgrade can be aborted.

**Stage 3: Dispatch.** If your module produces a schedule, the automated dispatch system assigns field teams to the conduits based on your period assignments.

## Input
The first line contains two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of endpoints and conduits output by Stage 1.
The next **m** lines each contain two integers u and v (1 ≤ u < v ≤ n), indicating a conduit between endpoint u and endpoint v.

## Output
If Stage 2 can successfully schedule the conduits, print `YES` on the first line. On the second line, print **m** integers from the set {1, 2, 3} separated by spaces, representing the period assigned to each conduit in the order they were provided in the input. If no such schedule is possible, print `NO`.

## Example
**Input:**
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
**Output:**
```
YES
1 2 3 3 2 1
```
