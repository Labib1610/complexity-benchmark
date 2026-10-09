# Problem A — Merchant Fleet

Time limit: 5 s   Memory limit: 256 MB

## Description

A merchant guild is organizing a season of trade. They need to schedule exactly $k$ voyages. To assemble a voyage, the guild must assign exactly one captain, one vessel, and one destination. 

Currently, the guild has:
- $k$ captains,
- $k$ vessels,
- $k$ destinations.

Each captain is identified by an integer from 1 to $k$. Similarly, each vessel and each destination is identified by an integer from 1 to $k$.

Not all combinations are viable. A captain might lack experience with a particular vessel, or a vessel might not be suited for the waters of a specific destination. The guild maintains a registry of $t$ approved voyage plans. Each approved plan consists of a specific captain, a specific vessel, and a specific destination that are known to work together.

The guild needs to select exactly $k$ approved voyage plans such that:
- Every captain is assigned to exactly one chosen voyage.
- Every vessel is used in exactly one chosen voyage.
- Every destination is targeted by exactly one chosen voyage.

Determine whether such a schedule can be formed. If it can, provide one valid selection of plans.

## Input

The first line of input contains two integers $k$ and $t$: the number of voyages to schedule, and the number of approved voyage plans in the registry.

The guild's charter mandates at least one voyage per season. The guild's port has a strict physical capacity of exactly 22 moorings, meaning the number of voyages $k$ will never exceed this structural limit. The number of approved plans $t$ can be as low as zero, and will not exceed the theoretical maximum where every captain, vessel, and destination can be combined together.

Each of the following $t$ lines contains three integers $C$, $V$, and $D$, representing an approved voyage plan utilizing captain $C$, vessel $V$, and destination $D$. No plan is listed more than once in the registry.

## Output

If a valid schedule of $k$ voyages can be formed, print `YES` on the first line. Then, print $k$ lines, each containing the three integers $C$, $V$, and $D$ of a chosen voyage plan. The chosen plans can be printed in any order. Any valid schedule meeting the requirements will be accepted.

If no such schedule is possible, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
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
2 1 2
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

In Example 2, both approved voyage plans require vessel 1. Consequently, vessel 2 can never be utilized, making a complete schedule impossible.
