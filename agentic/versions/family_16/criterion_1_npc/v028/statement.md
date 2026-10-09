# Problem A — Art Restoration

Time limit: 5 s   Memory limit: 256 MB

## Description

A museum is restoring **c** historical canvases. There are **p** unique elemental pigments available in the workshop. 

For each canvas, the restoration requires applying a strict sequence of layers. Each layer requires the exclusive use of a specific pigment for a given number of minutes. 

The restoration follows these protocols:
- The layers on a given canvas must be applied in the exact order prescribed. A layer on a canvas can only commence after its preceding layer is completely finished.
- There is exactly one specialized applicator for each pigment. Thus, any given pigment can be applied to at most one canvas at a time. (Different pigments may be applied to different canvases simultaneously).
- Once a layer's application begins, it cannot be interrupted; it must run continuously until that layer is complete.

Plan the restoration so that the minute at which the final canvas is completed is as early as possible. Report that earliest possible completion minute.

## Input

The first line contains two integers **c** and **p** (1 ≤ c ≤ 10, 1 ≤ p ≤ 10).
Each of the next **c** lines describes one canvas: an integer **L** (the number of layers) followed by **L** pairs of integers `pigment minutes` (1 ≤ pigment ≤ p, 1 ≤ minutes ≤ 1000), listing the canvas's layers in order.
The total number of layers across all canvases is at most 50.

## Output

Print a single integer: the earliest possible minute at which all canvases are completely restored.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note

In Example 1, two identical canvases each require pigments 1, 2, and 3 in that order (2 minutes each); the second canvas trails the first through the sequence and finishes at minute 8. In Example 3, the two canvases require different pigments and are restored in parallel, finishing at minute 4.
