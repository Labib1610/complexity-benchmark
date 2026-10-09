# Pre-Flight Manifest Diagnostic

Time limit: 2 s
Memory limit: 256 MB

## Description

You are building a validation module for a cargo routing system. The system receives a manifest of **j** shipments that must all be processed within a single operational window of **T** minutes.

Each shipment **i** (from 1 to **j**) requires a continuous processing duration of **p1** minutes at the Entry Checkpoint, followed by a continuous processing duration of **p2** minutes at the Exit Checkpoint. The processing must follow these physical rules:

1. A shipment must fully complete its Entry Checkpoint processing before it can begin its Exit Checkpoint processing.
2. A checkpoint can only process one shipment at a time.
3. All processing across both checkpoints for all shipments must begin and end within the **T**-minute operational window.

Before running the full scheduling engine, your validation module must scan the manifest for fundamental capacity violations. If a violation is found, the module halts and outputs a diagnostic code. For the test cases provided to this module, the manifest is guaranteed to trigger exactly one of the following violations:

- **Single Shipment Violation:** A specific shipment **i** cannot possibly complete within the **T**-minute window, even if it were the only shipment being processed, because its sequential processing times exceed the window. Output `JOB i`, where **i** is the 1-based index of the shipment.
- **Checkpoint Overcapacity:** A checkpoint cannot process all its assigned shipments within the **T**-minute window because the sum of the processing times at that checkpoint exceeds **T**. Output `LOAD c`, where **c** is 1 for the Entry Checkpoint or 2 for the Exit Checkpoint.

## Input

The first line contains two integers **j** and **T** (1 ≤ **j** ≤ 200000, 1 ≤ **T** ≤ 1000000000), representing the number of shipments and the operational window in minutes.
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ **p1**, **p2** ≤ 1000000), representing the required processing times at the Entry and Exit checkpoints for that shipment.

## Output

Print a single line containing the diagnostic code: `JOB i` (if **p1** + **p2** > **T** for shipment **i**) or `LOAD c` (if the sum of all processing times at checkpoint **c** exceeds **T**).

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

In Example 1, shipment 1 requires 70 minutes at the Entry Checkpoint and 60 minutes at the Exit Checkpoint. Because the exit processing cannot start before the entry processing finishes, the minimum time required for this shipment alone is 70 + 60 = 130. Since 130 > 100, `JOB 1` is the correct diagnostic code.

In Example 2, no single shipment exceeds the 150-minute window. However, the Entry Checkpoint must process four shipments of 50 minutes each without overlapping. Their combined time is 50 + 50 + 50 + 50 = 200. Since 200 > 150, `LOAD 1` is the diagnostic code.
