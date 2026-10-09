# Problem A — Regional Drill Deployment Plan

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate is preparing a full-scale readiness drill. The active roster consists of personnel with badge numbers running consecutively from 1 to 3q, where q is the target number of operational units to be formed.

Command maintains a historical registry of pre-cleared joint configurations. Each configuration lists the badge numbers of three personnel who have completed joint certification. Standing policy mandates that personnel may only be deployed in these exact registered groups; no ad-hoc groups are permitted. A single person might appear in many registered configurations, while some configurations might share personnel.

A deployment plan consists of choosing some configurations from the registry to activate. A plan is considered acceptable if and only if every person on the roster (from badge 1 to 3q) is assigned to an active configuration, and no person is assigned to more than one active configuration. This ensures full participation without any scheduling conflicts.

Determine whether the registry allows for an acceptable deployment plan. If it does, output one such plan. If no combination of registered configurations can meet the mandate, report that it is impossible.

## Input
The first line contains two integers **q** and **t** (1 ≤ q ≤ 200, 0 ≤ t ≤ 20000).
Each of the next **t** lines contains three integers a, b, and c (1 ≤ a < b < c ≤ 3q), representing the badge numbers in one pre-cleared configuration.

## Output
If an acceptable deployment plan exists, print `YES`. Then, print q lines, each containing the three badge numbers of a configuration chosen for the plan.
If no acceptable plan exists, print `NO`.

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
