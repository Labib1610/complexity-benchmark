# Phase 2: Full-Coverage Cell Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate follows a rigorous protocol for readiness drills. All active personnel are issued consecutive badge numbers starting from 1 up to a maximum of 3*q*.

Drill regulations impose absolute constraints on how personnel are grouped and deployed. Any deployed unit must be a three-person response cell. Furthermore, these units cannot be formed on the fly; they must be drawn directly from a master list of pre-cleared cells, which contains specific groups of exactly three operators who have previously completed joint certification.

When a drill is initiated, the directorate mandates full and exclusive participation. It is a violation of protocol for any operator between 1 and 3*q* to be left idle at the base. It is equally forbidden for any operator to be assigned to more than one active cell simultaneously. 

As the deployment coordinator, your responsibility is to analyze the total roster size 3*q* and the master list of pre-cleared cells. You must find a subset of the pre-cleared cells to activate such that the participation constraints are perfectly satisfied. If the provided master list cannot support such an arrangement, you must reject the drill plan.

## Input
The first line provides two integers *q* and *t* (1 ≤ *q* ≤ 200, 0 ≤ *t* ≤ 20000). The total roster size is 3*q* operators, and *t* is the number of pre-cleared cells on the master list.
Each of the following *t* lines provides three integers *a*, *b*, and *c* (1 ≤ *a* < *b* < *c* ≤ 3*q*), representing the badge numbers of the operators in a single pre-cleared cell.

## Output
If a valid deployment plan can be formed, print `YES` on the first line. Following that, output *q* lines, each containing the three badge numbers of an activated cell from your plan. If no valid plan can be formed, print `NO`.

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
