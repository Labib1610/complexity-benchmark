# Fabrication Contract Validator

Time limit: 2 s
Memory limit: 256 MB

## Description

A custom fabrication shop receives $j$ part requests that must be completed before a scheduled transport arrives in $T$ minutes. Fabrication requires two sequential operations: 3D printing (Operation 1) and thermal curing (Operation 2). The resin for a part must be printed completely before that part can be moved to the oven. The shop operates exactly one industrial 3D printer and exactly one thermal curing oven.

A proposed contract is immediately rejected if it contains a structural impossibility that guarantees the shop cannot finish before the transport arrives. The validation software must identify the precise reason for rejection by checking for two specific failure modes:

- A specific part requires more combined printing and curing time than the entire time before transport. If part $i$ (1-indexed) causes this, the software must output `JOB i`.
- A single piece of equipment requires more total active time across all $j$ parts than the time available before transport. If equipment $c$ (where $c$ is 1 for the printer, or 2 for the oven) causes this, the software must output `LOAD c`.

The test environment guarantees that every provided contract will trigger exactly one of these failure modes. Your task is to implement the validation software to output the correct failure code.

## Input

The first line of the input contains two integers $j$ and $T$ (1 ≤ $j$ ≤ 200000, 1 ≤ $T$ ≤ 1000000000), representing the number of parts and the minutes until the transport arrives.

The following $j$ lines each contain two integers $p_1$ and $p_2$ (1 ≤ $p_1$, $p_2$ ≤ 1000000). The $i$-th of these lines specifies the required 3D printing time ($p_1$) and thermal curing time ($p_2$) for part $i$.

## Output

Print a single line containing the failure code: either `JOB i` if part $i$ cannot be completed in time, or `LOAD c` if equipment $c$ lacks the capacity to finish all parts in time.

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, the first part requires 70 + 60 = 130 minutes of continuous processing. Since this exceeds the 100 minutes before the transport arrives, the software outputs `JOB 1`.

In Example 2, no individual part takes more than 150 minutes. However, the 3D printer (Operation 1) requires 50 + 50 + 50 + 50 = 200 minutes of total active work across all parts, which exceeds the 150 minutes available. Thus, the software outputs `LOAD 1`.
