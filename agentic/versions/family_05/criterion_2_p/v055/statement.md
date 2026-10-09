# Problem B — Quantum Key Distribution Network

Time limit: 2 s   Memory limit: 256 MB

## Description

You are configuring a quantum key distribution network. The hardware consists of **k** photon sources, **k** polarization waveplates, and **k** single-photon sensors. To establish a full-capacity network, you must configure exactly **k** independent communication channels. Each channel requires exactly one source, one waveplate, and one sensor.

Because of the extreme precision required, each component can be assigned to at most one channel. A full-capacity network must therefore utilize every source, every waveplate, and every sensor exactly once.

During hardware assembly, each photon source was permanently fiber-spliced to a dedicated waveplate to minimize optical loss. Consequently, a specific source can only route photons through its permanently attached waveplate, and no two sources share the same waveplate.

You are given a log of **t** successful calibration tests. Each test verifies that a specific combination of source, waveplate, and sensor can stably transmit data. You must determine if it is possible to select **k** verified combinations from the log to form a full-capacity network. If it is possible, you must output the configuration.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of components per type, and the number of calibration tests.

Each of the following **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k) representing a verified combination of source **x**, waveplate **y**, and sensor **z**. No combination is listed more than once. The input guarantees that for any given source **x**, all combinations involving **x** will feature the same waveplate **y**, and different sources will feature different waveplates.

## Output

If a full-capacity network can be configured, print `YES` on the first line. Then print **k** lines, each containing the three integers `x y z` of a chosen combination (the chosen combinations may be listed in any order). If multiple valid configurations exist, any of them will be accepted.

If no valid configuration can be formed, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
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
2 2 1
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
