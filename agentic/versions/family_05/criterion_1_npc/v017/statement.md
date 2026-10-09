# Problem A — Assembly Configuration Phase

Time limit: 5 s   Memory limit: 256 MB

## Description

The factory produces custom circuit boards in a three-stage automated pipeline.

**Stage 1: Material Preparation.** A handler prepares silicon wafers and routes them to the assembly floor.

**Stage 2: Assembly Configuration.** The system pairs up the factory's hardware. The floor has exactly **k** robotic arms, **k** optical sensors, and **k** control modules, each numbered 1 through **k**. A single production track requires exactly one arm, one sensor, and one module. Due to calibration constraints, only specific configurations of `(arm, sensor, module)` are viable. The system must select exactly **k** viable configurations to form **k** parallel production tracks, ensuring that every single arm, every sensor, and every module is assigned to exactly one track.

**Stage 3: Quality Assurance.** The assembled boards are sent to the testing bay for diagnostics.

Your software module is responsible only for Stage 2. Given the batch size **k** and the list of viable configurations logged from recent calibration tests, determine if it is possible to set up the **k** parallel tracks. If successful, output the configurations to be used so the pipeline can proceed to Stage 3.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of hardware units of each type, and the total number of viable configurations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a viable configuration consisting of robotic arm **x**, optical sensor **y**, and control module **z**. No configuration is listed more than once.

## Output

If a valid selection of **k** production tracks can be formed, print `YES` on the first line. Then, print **k** lines, each containing three integers `x y z` representing the hardware units of one chosen track. Any selection in which every arm, sensor, and module is used exactly once is accepted. The tracks may be printed in any order.

If no valid selection can be formed, print `NO`.

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

In Example 2, both viable configurations require optical sensor 1. This leaves optical sensor 2 unused, so it is impossible to form 2 valid tracks.
