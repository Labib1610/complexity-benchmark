# Thermal Regulation Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description
The station's thermal regulation system must be fully synchronized. The system consists of a set of thermal sources, numbered starting from 1. To ensure thermodynamic balance, the system also includes thermal sinks, matching the sources in quantity, numbered in a continuous sequence immediately following the sources. Every source and every sink is a distinct component, and safety protocols require that every single one of these components be engaged simultaneously in a single configuration.

A source may be linked with a sink only if that specific source-sink combination has been physically tested and verified. Unverified combinations are strictly prohibited. A source might be verified with multiple sinks, and a sink with multiple sources. The verification logs can be extensive and highly overlapping, with many more tested combinations than the configuration will ultimately use. None of that redundancy matters except through which exact combinations are verified — the counts, the overlaps, and the order of the logs are all incidental.

A valid configuration activates verified combinations such that every source and every sink is engaged in exactly one active combination. Each component is utilized exactly once; none can be left idle, and no component can be shared between two combinations. Determine if the verification logs allow for such a complete synchronization of all components. If so, output one such configuration; otherwise, report that the verified combinations cannot simultaneously engage every component.

## Input
The first line provides two integers $q$ and $t$. The value of $q$ is the quantity of thermal sources, which requires at least one unit to function and is capped at a facility maximum of one hundred thousand units. The value of $t$ represents the quantity of verified combinations, which can range from an empty log of zero up to a system limit of four hundred thousand records.

The following $t$ lines each provide two integers $a$ and $b$, representing a verified combination. The first identifier $a$ refers to a source, meaning its value is at least one and cannot exceed the total quantity of sources. The second identifier $b$ refers to a sink, meaning its value is strictly greater than the quantity of sources and cannot exceed the total quantity of components (which is exactly twice the quantity of sources).

## Output
If a complete synchronization is achievable, output `YES` on the first line, followed by $q$ lines each containing the two identifiers of an activated combination. If it is impossible, output `NO`.

## Example

**Input:**
```text
3 4
1 4
2 5
3 6
2 6
```

**Output:**
```text
YES
1 4
2 5
3 6
```
