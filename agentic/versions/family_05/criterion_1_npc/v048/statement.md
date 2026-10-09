# Problem A — Automated Assembly Pipeline

Time limit: 5 s   Memory limit: 256 MB

## Description

Our synthetic biology pipeline operates in four distinct phases: Procurement, Screening, Planning, and Incubation.

1. **Procurement:** The laboratory synthesizes raw materials to create three supply pools. For a batch size of **k**, we produce **k** distinct lipid chassis (numbered 1 to **k**), **k** distinct energy cores (numbered 1 to **k**), and **k** distinct genetic payloads (numbered 1 to **k**).
2. **Screening:** Because of biochemical interactions, not all combinations are stable. An automated system tests combinations and produces a log of **t** viable configurations. Each viable configuration consists of exactly one chassis, one core, and one payload.
3. **Planning:** The orchestration software must select configurations from the log to schedule the batch. To ensure zero waste in the current production cycle, the system must schedule exactly **k** configurations such that every single procured lipid chassis, energy core, and genetic payload from the first phase is utilized in exactly one scheduled configuration.
4. **Incubation:** The scheduled configurations are sent to the bioreactors for final assembly.

Your task is to implement the **Planning** phase. Given the batch size **k** and the log of **t** viable configurations from the Screening phase, determine whether a zero-waste schedule can be formed. If successful, output the configurations to be passed to the Incubation phase.

## Input

The first line contains two integers **k** and **t** (1 ≤ **k** ≤ 22, 0 ≤ **t** ≤ **k**·**k**·**k**): the batch size for each component type, and the number of viable configurations identified by the Screening phase.
Each of the following **t** lines contains three integers **c**, **e**, and **g** (1 ≤ **c**, **e**, **g** ≤ **k**), representing a viable configuration consisting of chassis **c**, energy core **e**, and genetic payload **g**. No configuration is listed more than once in the log.

## Output

If a zero-waste schedule of **k** configurations exists, print `YES` on the first line. Then, print **k** lines, each containing the three components `c e g` of a scheduled configuration. Any schedule that uses every lipid chassis, energy core, and genetic payload exactly once is accepted; the configurations may be printed in any order.

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

In Example 2, both viable configurations use energy core 1, so energy core 2 can never be utilized. A zero-waste schedule cannot be formed.
