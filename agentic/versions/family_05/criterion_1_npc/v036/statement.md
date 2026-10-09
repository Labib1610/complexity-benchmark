# Orbital Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description

A space agency is preparing to launch a fleet of exactly **k** communication satellites. The deployment relies on three sets of distinct resources: **k** frequency bands, **k** orbital positions, and **k** encryption keys. Each resource is identified by an integer from 1 to **k**.

A satellite is configured by assigning it one frequency band, one orbital position, and one encryption key. Only certain specific configurations (band, position, key) can successfully operate together. You are given the list of all viable configurations.

The fleet must be configured such that every frequency band is active on some satellite, every orbital position is occupied by some satellite, and every encryption key is utilized by some satellite. 

Determine whether it is possible to select **k** viable configurations that meet these requirements, and if so, output one such selection.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of satellites (which is also the number of resources in each set) and the number of viable configurations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a viable configuration consisting of frequency band **x**, orbital position **y**, and encryption key **z**. No configuration is listed more than once.

## Output

If a valid selection of **k** configurations exists, print `YES` on the first line, then print **k** lines, each containing the three integers `x y z` of one selected configuration. Any selection that utilizes all resources is accepted; the configurations may be printed in any order.

If no valid selection exists, print `NO`.

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

In Example 2, both viable configurations require orbital position 1, so orbital position 2 can never be occupied by any satellite.
