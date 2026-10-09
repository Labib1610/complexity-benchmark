# Simulation Roster Allocation

Time limit: 5 s
Memory limit: 256 MB

## Description
A regional crisis response agency is preparing a full-scale field simulation. To participate, the agency's personnel must be grouped into operational units. Every operational unit invariably requires exactly three staff members. The total headcount of the agency is exactly $3q$, meaning the staff can theoretically be divided into $q$ distinct units. Staff members are issued integer badges from $1$ up to the total headcount.

Operational protocols dictate that any unit deployed together must have prior joint training. The agency's historical archives contain a catalog of verified three-person combinations that meet this requirement. 

The coordinator's task is to select a subset of these verified combinations such that every single staff member is mobilized for the simulation. Because personnel cannot be in two places at once, no individual may be part of more than one selected unit. You must determine if such a deployment schedule is possible and, if so, output the chosen units. If the archive does not contain a set of combinations that perfectly partitions the entire staff, you must declare it impossible.

## Input
The first line contains two integers $q$ and $t$. The target number of units, $q$, is strictly positive. The agency's transportation fleet has a maximum capacity of 200 vehicles (one vehicle per unit), which serves as the upper bound for $q$. The number of archived combinations, $t$, is non-negative. The database storing these combinations has a strict architectural limit of 20,000 records, which $t$ will never exceed.

Each of the remaining $t$ lines contains three integers $a$, $b$, and $c$. These represent the badge numbers of three staff members who have completed joint training. For each combination, the badge numbers are provided in strictly ascending order. All badge numbers are valid, meaning they start at a minimum of 1 and do not exceed the total agency headcount.

## Output
If a valid deployment schedule can be formed, print `YES` on the first line. On the next $q$ lines, print the three badge numbers for each authorized unit. If there are multiple valid schedules, any of them will be accepted.
If it is impossible to schedule all personnel under the rules, print `NO`.

## Example
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
