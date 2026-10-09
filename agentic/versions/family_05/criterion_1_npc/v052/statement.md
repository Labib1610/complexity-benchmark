# Problem A — Operational Blueprint

Time limit: 5 s   Memory limit: 256 MB

## Description

At a construction facility, there are three distinct resource pools: personnel, equipment, and schedule blocks. The facility has exactly **k** workers, **k** equipment units, and **k** schedule blocks, each indexed from 1 to **k**.

Safety regulations prohibit arbitrary resource mixing. You are provided with a ledger of **t** approved operational blueprints. Each blueprint specifies exactly one worker, one equipment unit, and one schedule block that are authorized to interact.

To execute a complete facility run, you must activate a set of blueprints from the ledger. The execution is strictly governed by the facility's safety lock-out system:
- When a blueprint is activated, its specified worker, equipment unit, and schedule block become locked.
- A blueprint may only be activated if its worker, equipment unit, and schedule block are all currently unlocked.

Your objective is to find a set of activations that locks all **k** workers, all **k** equipment units, and all **k** schedule blocks. Determine whether it is possible to achieve this complete lock-out using only the blueprints provided in the ledger, and if so, list the blueprints that should be activated.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k), denoting the size of each resource pool and the number of approved blueprints in the ledger.
The following **t** lines each contain three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k). Each line represents an approved blueprint involving worker **x**, equipment unit **y**, and schedule block **z**. All blueprints in the ledger are distinct.

## Output

If a complete lock-out is possible, output `YES` on the first line. Following that, output **k** lines, each containing the three integers `x y z` of an activated blueprint. Any valid set of blueprints that achieves the objective is acceptable, and they may be listed in any order.

If no such set is possible, output `NO`.

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

In Example 2, both approved blueprints require equipment unit 1. Activating either blueprint locks equipment unit 1, preventing the other from being activated. Thus, equipment unit 2 can never be locked, making a complete lock-out impossible.
