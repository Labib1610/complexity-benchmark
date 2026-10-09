# Phase 2: Full-Coverage Cell Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate follows a strict three-phase protocol for full-scale readiness drills.

**Phase 1: Roster and Certification Audit**  
Before any drill, historical training records are analyzed. Operators are assigned consecutive badge numbers starting from 1 up to a total roster size of 3*q*. Command then generates a master list of pre-cleared three-person response cells. A cell is only added to this list if those exact three operators have completed joint certification. Ad-hoc groupings are strictly forbidden.

**Phase 2: Deployment Planning (Your Task)**  
You are responsible for the critical middle step. You receive the target number of cells *q* and the master list from Phase 1. You must select a subset of the pre-cleared cells to activate. The directorate mandates full participation: every operator from 1 to 3*q* must be deployed in exactly one activated cell. If an operator is left idle, or if an operator is scheduled in multiple active cells, the plan is rejected. You must either produce a perfect schedule or determine that the Phase 1 list makes this impossible.

**Phase 3: Execution and Debrief**  
Once your plan is approved, the chosen cells are dispatched to the field. Following the drill, command logs performance metrics for each active cell to guide future training.

Your software only needs to execute Phase 2.

## Input
The first line provides two integers *q* and *t* (1 ≤ *q* ≤ 200, 0 ≤ *t* ≤ 20000), where *q* dictates the required number of active cells (and thus a total roster of 3*q* operators), and *t* is the number of pre-cleared cells from Phase 1.
Each of the subsequent *t* lines contains three integers *a*, *b*, and *c* (1 ≤ *a* < *b* < *c* ≤ 3*q*), representing a single pre-cleared cell.

## Output
If Phase 2 can be successfully completed, print `YES` on the first line. Then, output *q* lines, each containing the three badge numbers of an activated cell from your plan. If no such plan can be formed, print `NO`.

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
