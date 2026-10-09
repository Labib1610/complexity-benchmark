# Problem A — Resonance of the Anchors

Time limit: 5 s
Memory limit: 256 MB

## Description

An interstellar alliance is preparing to activate a localized hyperspace field. To do this, they must establish a communication link across a specific set of primary space stations, known as Anchors. 

The alliance operates a number of space stations across a quadrant. The quadrant is mapped as a 10 by 10 coordinate grid, and each grid cell can house at most one station, establishing a strict upper limit on the total number of stations. Among these, certain stations are designated as Anchors. The alliance's high council requires one representative from each Anchor; because the high council's charter mandates a maximum of 10 members, the number of Anchors is correspondingly capped. There is always at least one Anchor.

Engineers have identified a list of potential hyperspace resonance channels that could be stabilized between specific pairs of stations. Stabilizing a channel requires a certain continuous energy expenditure. No two stations have more than one potential channel between them, and a station cannot form a channel with itself.

The hyperspace field will only activate if all Anchors can communicate with one another. A signal can pass between any two stations if they are directly connected by a stabilized channel, or indirectly connected via a sequence of stabilized channels. These channels can pass through non-Anchor stations, which act as optional relays. 

The engineers must choose a subset of the potential channels to stabilize. Stabilizing a channel incurs its energy cost exactly once, regardless of how much signal traffic passes through it. The goal is to select a subset such that all Anchors are mutually connected (i.e., a signal can travel between any two Anchors), while minimizing the sum of the energy costs of the stabilized channels.

## Input

The first line provides three integers: the total number of stations, the number of potential resonance channels, and the number of Anchors.
The second line contains a list of distinct integers representing the identifiers of the Anchors.
Each of the remaining lines (one for each potential channel) contains three integers: the identifiers of the two stations it connects, and the energy required to stabilize it.

The energy cost for any single channel is at least 1 and at most one million. It is guaranteed that it is possible to connect all Anchors using the available channels. Station identifiers are consecutive integers starting from 1.

## Output

Output a single integer: the minimum total energy required to ensure all Anchors are mutually connected.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, routing the channels through the optional relay station 4 (which costs 1+1+1 = 3 energy) is more efficient than linking the three Anchors directly (which would cost 4 energy). In Example 3, there is only one Anchor, so no channels need to be stabilized.
