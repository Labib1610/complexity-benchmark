# Airline Schedule (Route Integration)

Time limit: 2 s   Memory limit: 256 MB

## Description

An airline's daily operations pipeline consists of three distinct stages. You are responsible for implementing the second stage.

**Stage 1: Certification and Airframe Binding**
Before daily planning begins, the aviation authority finalizes crew assignments. Each of the **k** crews (numbered 1 to **k**) is permanently bound to exactly one of the **k** airframes (numbered 1 to **k**). No two crews are bound to the same airframe. This stage is already completed by an external system.

**Stage 2: Route Integration (Your Task)**
The automated dispatch system generates a set of **t** feasible deployment proposals based on meteorological data. Each proposal is a tuple `(x, y, z)` indicating that crew **x**, operating airframe **y**, can successfully complete route **z** (routes are numbered 1 to **k**). Because Stage 1 is strictly enforced, the proposals will only ever pair a crew with their officially bound airframe. 

Your module must process these proposals and select exactly **k** of them to form a complete daily schedule. A schedule is only valid if every crew, every airframe, and every route is utilized in exactly one selected proposal.

**Stage 3: Fuel Allocation**
If your module successfully finds a valid set of **k** proposals, it passes them to the refueling subsystem to prepare the fleet. If no such set exists, it must signal a failure so the pipeline can be aborted.

Determine if a complete schedule is possible, and if so, output the selected proposals.

## Input

The first line of input provides two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k), representing the number of crews/airframes/routes and the number of deployment proposals, respectively.
The following **t** lines each contain three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing a proposal where crew **x** flies airframe **y** on route **z**. All proposals are unique. As guaranteed by Stage 1, any given crew **x** will only ever appear with the same airframe **y** across all proposals, and different crews will appear with different airframes.

## Output

If Stage 2 can successfully form a complete schedule, print `YES` on the first line. Then, print **k** lines, each containing the three integers `x y z` of a selected proposal. The proposals can be printed in any order. Any valid schedule is accepted.

If it is impossible to complete Stage 2, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 2 1
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both crews' only feasible route is 1, so route 2 can never be covered.
