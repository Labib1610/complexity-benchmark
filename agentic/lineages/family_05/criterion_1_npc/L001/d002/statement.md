# Problem A — Crew Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

An operation requires coordinating three distinct pools of resources. Each pool contains exactly **k** elements:
- Operators, identified by integers 1 through k,
- Hardware units, identified by integers 1 through k,
- Mission phases, identified by integers 1 through k.

A deployment unit is formed by linking one Operator, one Hardware unit, and one Mission phase. Due to certification constraints, only specific (Operator, Hardware, Phase) combinations are authorized. You will receive a catalog of these authorized combinations.

Your task is to formulate an operational roster consisting of exactly **k** authorized combinations chosen from the catalog. To ensure operational safety, the chosen combinations must be entirely mutually exclusive. Specifically, no two combinations in the roster may share the same Operator, no two combinations may share the same Hardware unit, and no two combinations may share the same Mission phase.

Determine if such a roster can be formulated. If it can, provide one valid set of **k** combinations.

## Input

The first line provides two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k), representing the size of each resource pool and the total number of authorized combinations in the catalog.
The following **t** lines each contain three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), describing an authorized combination consisting of Operator **x**, Hardware unit **y**, and Mission phase **z**. No combination appears more than once in the catalog.

## Output

If a valid roster of **k** combinations can be formulated, output `YES` on the first line. Following this, output **k** lines, each containing three integers `x y z` corresponding to a chosen combination. Any valid roster meeting the mutual exclusivity conditions is acceptable. The combinations may be printed in any order.

If no such roster can be formulated, output `NO`.

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

In Example 2, both authorized combinations use Hardware unit 1. A roster of exactly 2 combinations cannot be formed without reusing Hardware unit 1, which violates the safety conditions.