# Phase 3: Drill Deployment Generation

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate is executing its automated workflow for the annual readiness drill. The workflow consists of four sequential phases.

In Phase 1, the HR system validates the active roster, identifying a pool of operators assigned sequential badge numbers starting from 1. 

In Phase 2, the compliance module processes years of raw training logs to extract a list of standardized, pre-cleared response units. Each unit always consists of exactly three operators who have completed joint certification. Ad-hoc groupings are strictly rejected by the compliance module.

Your task is to implement Phase 3. You are provided with the output of Phase 2: the total number of operators and the list of pre-cleared units. You must generate a deployment plan that activates a subset of these units. Leadership dictates that a drill is only valid if every single operator on the roster is committed without overlap. Therefore, your plan must assign every operator to exactly one activated unit. No operator may be left idle, and no operator may be shared between multiple activated units.

If you successfully generate a plan, it is passed to Phase 4, where the logistics engine allocates vehicles and gear to your chosen units. If the pre-cleared list cannot support a plan that covers the roster without omissions or redundancies, you must report the failure so the drill can be cancelled.

## Input
The first line contains two integers `q` and `t` (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000). The total number of operators on the roster is `3q`, with badges numbered 1 through `3q`.
Each of the next `t` lines represents a pre-cleared unit provided by Phase 2. Each line contains three integers `a`, `b`, and `c` (1 ≤ a < b < c ≤ 3q), representing the badge numbers of the operators in that unit.

## Output
If a valid Phase 3 deployment plan can be generated, print `YES` on the first line. Then, print `q` lines, each containing the three badge numbers of an activated unit in your plan. 
If no such plan is possible, print `NO`.

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
