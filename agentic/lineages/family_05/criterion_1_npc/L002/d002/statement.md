# Problem A — Optical Switch Configuration

Time limit: 5 s   Memory limit: 256 MB

## Description

An optical network switch routes data. The hardware provides **k** input ports (numbered 1 to **k**), **k** output ports (numbered 1 to **k**), and **k** distinct optical frequencies (numbered 1 to **k**).

Due to hardware limitations, only certain specific transmission pathways are physically viable. You are provided with a list of **t** viable pathways. Each pathway is defined by a triplet `(u, v, w)`, meaning it connects input port `u` to output port `v` using frequency `w`.

Your task is to activate exactly **k** pathways from the provided list to achieve full capacity. To avoid interference and hardware faults, the chosen set of exactly **k** pathways must be perfectly independent across all three dimensions. Specifically:
- No two activated pathways may use the same input port.
- No two activated pathways may use the same output port.
- No two activated pathways may use the same optical frequency.

Determine whether such a full-capacity routing configuration is possible, and if so, output one valid set of **k** activated pathways.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the scale of the switch (number of ports and frequencies), and the number of viable pathways in the list.
Each of the following **t** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v, w ≤ k), representing a viable pathway connecting input port **u** to output port **v** using frequency **w**. No pathway is listed more than once.

## Output

If a full-capacity configuration of exactly **k** pathways exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers `u v w` of an activated pathway. Any configuration that meets all requirements is accepted; the pathways may be printed in any order.

If no such configuration exists, print `NO`.

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

In Example 2, both viable pathways connect to output port 1. Activating exactly 2 pathways from the list would require choosing both, which violates the requirement that no two activated pathways may use the same output port. Therefore, no valid configuration exists.