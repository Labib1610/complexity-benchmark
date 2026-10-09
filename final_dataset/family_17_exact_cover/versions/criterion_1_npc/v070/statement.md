# Problem A — Phase 2: Allocation Step for the Readiness Audit

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate is conducting its Annual Readiness Audit. This audit is structured into a rigid three-phase pipeline.

Phase 1, the Credential Review, has just finished running on the central servers. It identified exactly $3q$ active personnel (assigned sequential IDs from $1$ to $3q$) and cross-referenced their training logs to produce a ledger of $t$ compatible three-person squads. A squad is only listed in this ledger if all three members have previously completed joint certification.

Your task is to implement Phase 2: the Roster Allocation Step. You must process the ledger from Phase 1 and attempt to select a subset of the compatible squads such that every single person from the $3q$ active personnel is assigned to exactly one selected squad. No person may be left out, and no person can be assigned to multiple squads. 

If you successfully generate this schedule, it will be passed to Phase 3, the Field Dispatch module, which will broadcast deployment coordinates to the selected squads. If it is impossible to form a schedule that perfectly allocates everyone using only the squads in the ledger, Phase 2 must halt the pipeline and report a failure.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), where $q$ dictates the target number of squads to select and $t$ is the number of compatible squads found during Phase 1.

Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the IDs of three personnel who form a compatible squad in the ledger.

## Output
If a valid schedule for Phase 2 can be formed, print `YES` on the first line. Following that, print $q$ lines, each containing the three personnel IDs of a selected squad. 
If no such schedule can be formed, print `NO`.

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
