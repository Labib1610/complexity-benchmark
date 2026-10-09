# Problem A — Orbital Assembly Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description
An orbital shipyard is assembling a vessel from $n$ standard structural modules. The assembly process is constrained by the availability of lifting equipment and the structural integrity of the vessel during construction:

- The shipyard operates in discrete daily shifts. Placing any single module takes exactly one full shift.
- There are $M$ identical grav-cranes. Each crane can place at most one module per shift.
- You have a strict deadline of $T$ shifts to complete the entire assembly.
- The design dictates that certain modules must be anchored to others. If a module $b$ requires module $a$ as an anchor, module $a$ must be placed during a shift strictly prior to the shift in which module $b$ is placed. Modules placed during the same shift are maneuvered simultaneously and cannot serve as anchors for one another.

You must determine if it is possible to assign every module to a specific shift (numbered 1 through $T$) such that no shift requires more than $M$ cranes, and all anchoring requirements are satisfied. 

## Input
The first line contains four integers: $n$ (the total number of modules), $M$ (the number of available grav-cranes), $T$ (the number of shifts before the deadline), and $m$ (the number of anchoring requirements).
The following $m$ lines each contain two integers $a$ and $b$, indicating that module $a$ must be placed in a strictly earlier shift than module $b$. Modules are identified by integers from 1 to $n$.

## Output
If the vessel can be completely assembled within $T$ shifts, print `YES` on the first line. On the second line, print $n$ integers: the shift number (from 1 to $T$) assigned to each module from 1 to $n$. If it cannot be assembled within the deadline, print `NO`.

## Example 1

**Input:**
```
5 2 3 4
1 2
1 3
2 4
3 5
```

**Output:**
```
YES
1 2 2 3 3
```
