# Problem A — System Calibration

Time limit: 5 s   Memory limit: 256 MB

## Description

You are calibrating an industrial system that operates using a set of tuning profiles. Every profile is defined by three parameters: its frequency, its voltage, and its phase. Each parameter is represented by an integer from 1 to **k**.

You are provided with a registry of **t** specific profiles that are currently supported by the hardware. No two profiles in the registry have the exact same combination of frequency, voltage, and phase.

Your objective is to extract a subset of exactly **k** profiles from the registry to form a "balanced configuration". In a balanced configuration, every parameter value from 1 to **k** must be utilized exactly once across the chosen profiles. 

Since the parameter values form a perfect sequence from 1 to **k**, the problem exhibits strict regularity. Because a balanced configuration requires exactly one profile for each frequency, you can approach the task by processing the frequencies sequentially from 1 to **k**. For each frequency, you simply select one compatible profile from the registry. To achieve full balance, your selections must ensure that the **k** chosen profiles collectively feature exactly one of each voltage from 1 to **k**, and exactly one of each phase from 1 to **k**.

Determine whether it is possible to form a balanced configuration from the registry, and if so, output one valid configuration.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of distinct values for each parameter, and the number of profiles in the registry. 
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a registry profile with frequency **x**, voltage **y**, and phase **z**. No profile is listed more than once.

## Output

If a balanced configuration of **k** profiles exists, print `YES` on the first line, then print **k** lines, each containing the three parameters `x y z` of one chosen profile. Any valid configuration is accepted; the profiles may be printed in any order.

If no balanced configuration exists, print `NO`.

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

In Example 2, both available profiles use voltage 1. When you select a profile for frequency 1 and a profile for frequency 2, they will inevitably conflict on voltage, making a balanced configuration impossible.
