# Problem A — Spatial Sensor Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description

You are deploying a sensor network within a cubic testing chamber. The chamber's space is discretized into **k** X-planes, **k** Y-planes, and **k** Z-planes. The planes in each dimension are numbered from 1 to **k**. Due to interference limits, the chamber can support a maximum of 22 planes per dimension (and requires at least 1).

A sensor can only be placed at specific stable coordinates where the environmental noise is low. You have mapped **t** such stable coordinates. There might be no stable coordinates, or all theoretically possible k·k·k coordinates might be stable.

Your objective is to activate a network of exactly **k** sensors from your mapped list. To ensure full spatial coverage without resonance cascade, the network must satisfy:
- Every X-plane must contain exactly one active sensor.
- Every Y-plane must contain exactly one active sensor.
- Every Z-plane must contain exactly one active sensor.

Determine if such a deployment is possible, and if so, report the coordinates of the chosen sensors.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of planes in each dimension, and the number of stable coordinates.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), describing a stable coordinate located at X-plane **x**, Y-plane **y**, and Z-plane **z**. No coordinate appears more than once in the list.

## Output

If a valid deployment of **k** sensors is possible, output `YES` on the first line. Then, output **k** lines, each containing the three integers `x y z` of a chosen sensor's coordinate. Any valid selection where every X-plane, Y-plane, and Z-plane contains exactly one active sensor is accepted. The chosen coordinates can be printed in any order.

If no such deployment exists, output `NO`.

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

In Example 2, both stable coordinates require Y-plane 1, meaning Y-plane 2 can never contain an active sensor.