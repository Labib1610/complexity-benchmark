# Problem A — Pipeline Hardware Allocation

Time limit: 5 s   Memory limit: 256 MB

## Description

A manufacturing facility builds custom circuit boards through a three-step automated process.

**Step 1: Ingestion.** Raw materials are transported to the main floor.

**Step 2: Equipment Synchronization.** The floor houses exactly **k** mechanical actuators, **k** laser scanners, and **k** processing units. For each equipment category, the items are labeled with integers from 1 to **k**. A single, independent manufacturing track is formed by linking together exactly one mechanical actuator, one laser scanner, and one processing unit. However, due to complex timing dependencies, a track can only function if the specific combination of (actuator, scanner, processing unit) is explicitly listed as a certified configuration. 
Your objective is to activate exactly **k** independent tracks. To achieve this, you must choose **k** certified configurations from the provided list such that every individual mechanical actuator, every individual laser scanner, and every individual processing unit is incorporated into exactly one track.

**Step 3: Diagnostics.** Completed boards are tested.

Your module handles Step 2. Given the quantity **k** and the list of certified configurations, determine if the facility can successfully deploy all of its equipment into **k** functional tracks. If so, output the configurations to be activated.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k), where **k** is the quantity of equipment in each category, and **t** is the number of certified configurations available.
Then, **t** lines follow. Each line consists of three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), indicating that mechanical actuator **x**, laser scanner **y**, and processing unit **z** can operate together as a certified configuration. All listed configurations are unique.

## Output

If all equipment can be successfully partitioned into **k** functional tracks, print `YES` on the first line. On the following **k** lines, print three integers `x y z` per line, representing the equipment used in each activated track. Any valid partition where each piece of equipment appears in exactly one track will be accepted. You may print the chosen tracks in any order.

If there is no way to deploy all equipment into **k** tracks, print `NO`.

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

In Example 2, both certified configurations require laser scanner 1. This means laser scanner 2 cannot be deployed, making it impossible to form 2 valid tracks.