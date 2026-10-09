# Problem A — Industrial Alchemy

Time limit: 5 s   Memory limit: 256 MB

## Description

You manage a specialized chemical plant that needs to fulfill a massive contract. The contract requires a production schedule consisting of exactly **k** product batches.

Your facility works with **k** distinct raw materials, **k** distinct catalysts, and **k** distinct finishing treatments. Each of these resources is identified by an integer from 1 to **k**.

In your database, there are **t** known viable synthesis protocols. Each protocol specifies exactly one raw material (**m**), one catalyst (**c**), and one finishing treatment (**f**). No two protocols in the database are identical.

You must select exactly **k** protocols from your database to form the schedule. To prevent contamination and equipment fatigue, the schedule must satisfy this strict diversity condition:
- No two chosen protocols may use the same raw material.
- No two chosen protocols may use the same catalyst.
- No two chosen protocols may use the same finishing treatment.

Determine whether it is possible to select exactly **k** protocols from your database that form a valid schedule, and if so, report one such selection.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of required batches (which is also the number of available materials, catalysts, and treatments), and the number of known protocols. 
Each of the next **t** lines contains three integers **m**, **c**, **f** (1 ≤ m, c, f ≤ k), representing an available protocol that uses raw material **m**, catalyst **c**, and finishing treatment **f**. No protocol is listed more than once.

## Output

If a valid schedule of **k** protocols exists, print `YES` on the first line, then print **k** lines, each containing the three integers `m c f` of one chosen protocol. Any selection meeting the conditions is accepted; the protocols may be printed in any order.

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

In Example 2, both available protocols use the same catalyst (1). Choosing both would violate the diversity condition, so it is impossible to schedule 2 valid batches.