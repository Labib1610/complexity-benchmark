# Problem A — System Upgrade Isolation

Time limit: 5 s   Memory limit: 256 MB

## Description

Before a major infrastructure upgrade can proceed, an automated diagnostic tool runs a hardware compatibility check on the server cluster. It evaluates connections between the data feeds, processing cores, and memory banks. The tool generates a log of viable routing pathways that can operate without interference. Each viable pathway securely links one data feed, one processing core, and one memory bank.

Your task is to handle the next phase of the upgrade: pathway allocation. The cluster contains exactly **k** data feeds, **k** processing cores, and **k** memory banks (each numbered 1 through **k**). You will receive the log of viable pathways. You must lock in exactly **k** pathways from this log to form a complete isolation matrix. To satisfy the matrix requirements, every single data feed, every single processing core, and every single memory bank must each be incorporated into a locked pathway, with no component left unused and no component shared among multiple pathways.

Once you have determined the allocation, the network controller will take over. It will physically partition the hardware according to your selection and begin the software upgrade. If it is impossible to form a complete isolation matrix from the provided log, the upgrade must be aborted.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of components of each type and the number of viable routing pathways identified by the diagnostic tool.

Each of the next **t** lines contains three integers **f**, **c**, and **m** (1 ≤ f, c, m ≤ k), representing a viable pathway connecting data feed **f**, processing core **c**, and memory bank **m**. No pathway is listed more than once in the log.

## Output

If a complete isolation matrix can be formed, print `YES` on the first line. Then, print **k** lines, each containing the three integers `f c m` corresponding to one of the locked pathways. The pathways may be printed in any order. Any valid selection that meets the matrix requirements is accepted.

If no such selection is possible, print `NO`.

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

In Example 2, both viable pathways require processing core 1, meaning processing core 2 would be left unused.
