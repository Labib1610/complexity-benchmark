# Problem A — Backbone Trenching for the Control Vault

Time limit: 5 s
Memory limit: 256 MB

## Description
The commissioning of a new control vault follows a strict three-phase protocol.

**Phase 1: Logical Topology**
The Systems Engineering team defines the vault's operational requirements. They output a design consisting of $n$ distinct control modules (numbered 1 through $n$) and a list of $m$ required point-to-point communication channels between specific pairs of modules. 

**Phase 2: Physical Integration (Your Task)**
You must map the logical design into the physical space. The vault contains a single straight equipment trench divided into exactly $n$ consecutive mounting bays, numbered 1 to $n$ from one end to the other. You must assign exactly one module to each bay. 

A cable tray runs parallel to the trench. For every communication channel defined in Phase 1, a physical harness must be run through the tray between the bays containing the two linked modules. The length of a harness is determined entirely by the separation of the bays: adjacent bays require 1 unit of harness, bays separated by one other bay require 2 units, and so on (the length is the absolute difference between their bay numbers). 

Procurement has allocated a strict total harness budget of $B$ units for the entire vault. Your goal is to determine if there is a valid assignment of modules to bays such that the grand total length of all required harnesses is at most $B$.

**Phase 3: Fabrication and Assembly**
If your placement is valid, the Fabrication team cuts the cables to your exact specifications, and the Installation team mounts the modules. If no such placement exists, you must reject the design, forcing Systems Engineering to redesign the logical topology.

## Input
The first line contains three integers $n$, $m$, and $B$ — the number of modules, the number of communication channels, and the total harness budget.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that Phase 1 requires a communication channel between module $u$ and module $v$.

## Output
If the Physical Integration phase can be completed within the budget, print `YES` on the first line. On the second line, print $n$ space-separated integers representing your bay assignments: the $i$-th integer must be the bay number (from 1 to $n$) where module $i$ is installed. If there are multiple valid assignments, any one that satisfies the budget is acceptable.
If no assignment can meet the budget, print `NO`.

## Example

**Input**
```
4 3 4
1 2
1 3
1 4
```

**Output**
```
YES
2 1 3 4
```

**Note on the Example**
Module 1 is assigned to bay 2, module 2 to bay 1, module 3 to bay 3, and module 4 to bay 4.
The required harnesses are:
- Between module 1 (bay 2) and module 2 (bay 1): length $|2 - 1| = 1$
- Between module 1 (bay 2) and module 3 (bay 3): length $|2 - 3| = 1$
- Between module 1 (bay 2) and module 4 (bay 4): length $|2 - 4| = 2$
The total harness length is $1 + 1 + 2 = 4$, which is exactly the budget $B$.
