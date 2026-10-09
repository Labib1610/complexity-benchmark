# Directorate Drill Pipeline

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate's upcoming operational drill is executed through an automated three-phase pipeline. Your software module is responsible for the critical second phase.

**Phase 1: Asset Certification (Completed)**
The diagnostic suite has already enumerated the available hardware, identifying $q$ controllers (assigned identifiers $1$ through $q$) and $q$ platforms (assigned identifiers $q+1$ through $2q$). It has performed handshake tests between them, producing a raw log of $t$ certified pairings that successfully established a connection. This log is the input provided to your module.

**Phase 2: Roster Synthesis (Your Task)**
Your module must filter the raw log of certified pairings to construct the active drill roster. The theoretical search space of all possible subsets is astronomically large (up to $2^{400,000}$), but the constraints are strict. To form a valid roster, you must select a subset of the pairings such that every single controller and every single platform is engaged exactly once. If any hardware asset is left out of the selection, or if any asset is included in more than one selected pairing, the roster is invalid.

**Phase 3: Execution (Downstream)**
If your module successfully synthesizes a valid roster, it will be ingested by the hypervisor to initialize the drill. If the available pairings make it impossible to satisfy the constraints, your module must abort the pipeline so that a manual hardware review can be triggered.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a certified pairing between controller $a$ and platform $b$ from Phase 1.

## Output
If a valid roster can be synthesized for Phase 3, print `YES` followed by $q$ lines, each containing the two identifiers of a chosen pairing from the active roster. Otherwise, print `NO` to abort the pipeline.

## Example

**Input**
```text
3 4
1 4
2 5
3 6
1 5
```

**Output**
```text
YES
1 4
2 5
3 6
```
