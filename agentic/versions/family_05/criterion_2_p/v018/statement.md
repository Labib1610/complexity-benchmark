# Problem B — Synchronized Deployment

Time limit: 2 s   Memory limit: 256 MB

## Description

A logistics company maintains a registry of approved deployment protocols. Each protocol specifies three components: a foreman (numbered 1 to **k**), a transport vehicle (numbered 1 to **k**), and a work sector (numbered 1 to **k**).

Due to strict certification requirements, any given foreman is only ever certified to operate one specific transport vehicle. Additionally, the company's vehicle fleet is exclusively assigned, meaning no two foremen are certified for the same vehicle. Consequently, in the registry of approved protocols, whenever a specific foreman is listed, they are always paired with their uniquely assigned vehicle.

The company is planning a massive synchronized operation. The goal is to activate a subset of exactly **k** protocols from the registry. A valid activation must deploy every single foreman, utilize every single transport vehicle, and cover every single work sector exactly once.

Determine whether it is possible to select such a set of **k** protocols. If a valid configuration exists, you must also provide one such selection.

## Input

The first line provides two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of foremen/vehicles/sectors, and the total number of approved deployment protocols in the registry.

The next **t** lines each contain three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing an approved protocol consisting of foreman **x**, vehicle **y**, and sector **z**. No protocol is listed more than once. As guaranteed, all protocols involving foreman **x** will feature the same vehicle **y**, and no other foreman will be paired with vehicle **y**.

## Output

If it is possible to select **k** protocols meeting all requirements, print `YES` on the first line. Then, output **k** lines, each containing the three integers `x y z` of a selected protocol. The protocols may be printed in any order. Any valid selection is accepted.

If no such selection is possible, print `NO`.

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
