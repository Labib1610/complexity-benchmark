# Problem A — Industrial Alchemy

Time limit: 5 s   Memory limit: 256 MB

## Description

You manage a specialized chemical plant that needs to fulfill a massive contract. The contract requires a production schedule. The number of product batches required is **k**. Due to facility constraints, **k** is bounded by a minimum operational threshold of 1 batch and a maximum physical capacity of 22 batches.

Your facility works with **k** distinct base compounds, **k** distinct reagents, and **k** distinct thermal profiles. Each of these resources is identified by an integer from 1 to **k**.

In your database, there are **t** known viable synthesis pathways. The number of known pathways ranges from a minimum of 0 up to a theoretical maximum of **k**·**k**·**k**. Each pathway specifies exactly one base compound (**m**), one reagent (**c**), and one thermal profile (**f**). No two pathways in the database are identical.

You must select a subset of pathways from your database to form the schedule. To ensure a balanced workload and prevent cross-contamination, the schedule must satisfy this strict condition:
- The chosen subset of pathways must collectively utilize every available base compound exactly once, every available reagent exactly once, and every available thermal profile exactly once.

Determine whether it is possible to select such a subset of pathways from your database that form a valid schedule, and if so, report one such selection.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the required number of resource types and the number of known pathways. 
Each of the next **t** lines contains three integers **m**, **c**, and **f** (1 ≤ m, c, f ≤ k), representing an available pathway that uses base compound **m**, reagent **c**, and thermal profile **f**. No pathway is listed more than once.

## Output

If a valid schedule exists, print `YES` on the first line, then print **k** lines, each containing the three integers `m c f` of one chosen pathway. Any selection meeting the conditions is accepted; the pathways may be printed in any order.

If no such schedule exists, print `NO`.

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

In Example 2, both available pathways use the same reagent (1). Choosing both would violate the condition that every reagent is utilized exactly once, so it is impossible to form a valid schedule.