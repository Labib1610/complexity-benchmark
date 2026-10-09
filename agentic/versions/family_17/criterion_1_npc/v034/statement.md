# Problem A — Regional Drill Deployment Plan

Time limit: 5 s   Memory limit: 256 MB

## Description
The regional emergency directorate is preparing a full-scale readiness drill. Every certified responder on the active roster must be committed to the exercise. Leadership has mandated that the entire roster must be active simultaneously, and no responder may be assigned to more than one task force at a time.

A standard task force is formed by assigning a driver, a medic, and a coordinator. Over the years, specific groups of responders have completed joint certification. Standing policy permits command to field a task force only if those specific three individuals appear together as a pre-cleared group in the historical database. Ad-hoc groups are not permitted. A single responder might be part of many different pre-cleared groups.

A deployment plan consists of a selection of the pre-cleared groups. The plan is acceptable only when the selected groups collectively include every single responder on the roster, with each responder appearing in merely one active task force. No responder can be left out, and no responder can be shared between active task forces.

Your task is to determine whether the pre-cleared groups can be selected to meet these requirements, and if so, to produce one acceptable deployment plan. If the historical database cannot fulfill the requirements, report that no acceptable plan exists.

The agency's motor pool limits the number of deployed task forces, $q$, to a maximum of two hundred, while a drill requires at least one. The historical database contains $t$ pre-approved groups, ranging from zero up to twenty thousand. Responders are identified by consecutive badge numbers starting from 1 up to exactly three times $q$. Within each pre-approved group, the badge numbers are listed in strictly increasing order.

## Input
The first line contains two integers $q$ and $t$, representing the number of required task forces and the number of pre-approved groups.
Each of the next $t$ lines contains three integers $a$, $b$, and $c$, representing the badge numbers of the responders in one pre-approved group.

## Output
If a valid selection exists, print `YES`, then $q$ lines each with the three badge numbers of one chosen group.
Otherwise print `NO`.

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
