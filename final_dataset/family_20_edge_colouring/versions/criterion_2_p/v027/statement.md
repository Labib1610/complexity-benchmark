# Orbital Telemetry Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description
In low-earth orbit, a constellation of satellites relays telemetry to a network of terrestrial antennas. Each scheduled transmission involves exactly one satellite and exactly one terrestrial antenna. A satellite may participate in multiple transmissions, and an antenna may receive from multiple transmissions, but all communication is strictly between the orbital network and the terrestrial network.

To avoid signal interference, transmissions are modulated onto discrete frequency channels, numbered 1, 2, 3, and so on. The hardware imposes a strict isolation requirement: if a satellite is involved in multiple transmissions, each must use a distinct frequency channel. Similarly, if a terrestrial antenna receives multiple transmissions, each must be assigned a different channel. Any two transmissions sharing a satellite or sharing an antenna must operate on different channels.

Let $K$ be the peak transmission load, defined as the maximum number of transmissions involving any single satellite or any single terrestrial antenna. Because of the isolation requirement, it is physically impossible to schedule all transmissions using fewer than $K$ channels.

Your task is to configure the network by assigning an integer channel identifier from 1 to $K$ to every transmission, guaranteeing that no satellite or terrestrial antenna is ever assigned the same channel twice. (The two-sided nature of the network guarantees that an assignment using exactly $K$ channels is always possible).

## Input
First line: three integers nL, nR, m (1 ≤ nL, nR ≤ 100000, 0 ≤ m ≤ 400000).
Next m lines: two integers u v (1 ≤ u ≤ nL, 1 ≤ v ≤ nR), indicating a transmission between satellite u and terrestrial antenna v.

## Output
Print `YES`, then a line with m integers in 1..K — the frequency channel assigned to transmission i in input order.

## Example

### Input
```text
3 3 5
1 1
1 2
2 2
2 3
3 3
```

### Output
```text
YES
1 2 1 2 1
```
