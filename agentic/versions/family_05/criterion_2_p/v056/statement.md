# Orbital Mission Scheduling

Time limit: 2 s
Memory limit: 256 MB

## Description
An aerospace agency is preparing exactly **k** orbital missions. Each mission requires allocating three types of resources, each indexed from 1 to **k**:
- **k** payloads,
- **k** launch rockets,
- **k** telemetry bands.

A viable mission configuration consists of one payload, one launch rocket, and one telemetry band. You are given a catalog of all physically viable configurations. Due to payload mass and adapter compatibility, every payload is exclusively compatible with exactly one specific launch rocket, and no two payloads are compatible with the same launch rocket.

To comply with safety protocols, the catalog is guaranteed to satisfy the following limits:
- No telemetry band is involved in more than **k** viable configurations.
- No launch rocket is involved in more than **k** viable configurations.

Your objective is to finalize exactly **k** mission configurations such that every payload, every launch rocket, and every telemetry band is utilized exactly once. Determine if a complete allocation is achievable, and if so, output one valid set of configurations.

## Input
The first line provides two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k), representing the number of each resource type and the total number of viable configurations in the catalog.

Each of the following **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), describing a viable configuration comprising payload **x**, launch rocket **y**, and telemetry band **z**. No configuration is repeated. Consistent with adapter compatibility, all viable configurations for a particular payload will list the identical launch rocket, and distinct payloads will list distinct launch rockets.

## Output
If a complete allocation can be formed, print `YES` on the initial line. Following that, print **k** lines, each containing three integers `x y z` corresponding to a chosen configuration. The configurations may be printed in any order. Any valid complete allocation is acceptable.

If no such allocation can be formed, print `NO`.

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
