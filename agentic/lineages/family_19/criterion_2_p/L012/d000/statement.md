# Problem B — Freight Assignment over a Corridor System

Time limit: 2 s   Memory limit: 256 MB

## Description
A logistics operator is tasked with moving a specific volume of a single type of cargo through a system of sorting facilities. These facilities are linked by one-way transit corridors. Each corridor has a strict upper bound on the number of cargo units it can handle in a single shift, due to vehicle limitations. The operator must move exactly the required volume of cargo from the dispatch facility to the receiving facility within one shift.

The assignment of cargo must follow these operational rules:
- The number of units assigned to any corridor must be a non-negative integer that is no greater than the corridor's upper bound.
- Sorting facilities (excluding the dispatch and receiving facilities) cannot hold cargo between shifts. Therefore, the total number of units arriving at such a facility via its incoming corridors must exactly equal the total number of units departing via its outgoing corridors.
- The dispatch facility must send out exactly the required volume of cargo. If any corridors lead back into the dispatch facility, the assignment must be adjusted so that its total outgoing cargo minus its total incoming cargo is exactly the required volume.
- Similarly, the receiving facility must absorb exactly the required volume, meaning its total incoming cargo minus its total outgoing cargo must equal the required volume.

You must determine an assignment of cargo units to each corridor that fulfills the required volume while strictly adhering to the upper bounds and the facility rules. If no such assignment is possible in a single shift, you must report this.

## Input
Line 1: Three integers `n`, `m`, and `1`, representing the number of facilities, the number of corridors, and the number of cargo types.
Line 2: Three integers `s`, `t`, and `d`, representing the dispatch facility, the receiving facility, and the required total volume of cargo.
Next `m` lines: Three integers `u`, `v`, and `limit`, detailing a one-way corridor from facility `u` to facility `v` with a maximum payload of `limit` cargo units.

## Output
First line: `YES` if the assignment is possible, or `NO` otherwise.
If `YES`, print a second line containing `m` integers — the assigned number of cargo units for each corridor, in the exact order the corridors were provided in the input.

## Example

**Input**
```text
4 5 1
1 4 5
1 2 3
1 3 4
2 3 1
2 4 2
3 4 3
```

**Output**
```text
YES
2 3 0 2 3
```
