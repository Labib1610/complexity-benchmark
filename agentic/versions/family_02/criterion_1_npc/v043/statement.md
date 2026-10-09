# Problem A — Control Panel Commissioning

Time limit: 2 s   Memory limit: 256 MB

## Description

A central control panel contains **n** two-way switches, indexed from 1 to **n**. You must assign every switch to either position 1 or position 0 before the system can operate. No switch may be left unassigned, and there are no intermediate positions.

During the commissioning phase, auditors generated **m** operational constraints. Each constraint monitors exactly three specific switch-position requirements. A requirement consists of a switch index and a desired position (either 1 or 0). 

The mechanics of a constraint are as follows:
- It continuously checks the global state of its three specified requirements.
- Because a constraint with a matched requirement imposes nothing further, matching just **at least one** of the three requirements instantly clears the entire constraint.
- If the panel's configuration contradicts all three of the requirements, the constraint triggers a system halt.

The same switch typically appears across many constraints, sometimes demanded to be in position 1 by one constraint and position 0 by another. Therefore, assigning a position to a heavily-used switch can simultaneously clear a large block of constraints. The constraints may overlap heavily or barely at all — none of that matters except through the exact requirements each constraint lists. 

Your task is to determine whether there is a single global configuration for all **n** switches that clears **every** constraint simultaneously. If such a configuration exists, you must provide one; otherwise, the constraint set is over-constrained. Clearing the constraints individually is trivial since any single requirement clears its constraint — the difficulty is finding one configuration consistent with all of them at once.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400), representing the number of switches and the number of constraints.
Each of the following m lines represents a single constraint by listing three non-zero integers l₁, l₂, l₃. 
The absolute value of each integer |lᵢ| indicates the switch index (1 to n). 
The sign of the integer indicates the required position: a positive value means the switch is required to be in position 1, and a negative value means the switch is required to be in position 0.

## Output
If there is no configuration that clears all constraints, print a single line with `NO`.
Otherwise, print `YES` on the first line. On the second line, print n space-separated integers s₁, s₂, …, sₙ (where each sᵢ ∈ {0, 1}), representing the position of each switch from 1 to n. If multiple valid configurations exist, any valid configuration is accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each constraint lists exactly three requirements. The same switch index may appear more than once within a single constraint.
