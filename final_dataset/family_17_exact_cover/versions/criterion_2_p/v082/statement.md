# Thermal Regulation Grid

Time limit: 2 s   Memory limit: 256 MB

## Description
You are finalizing the thermal management layout for a newly constructed spacecraft. The ship contains $2q$ critical components. The components numbered $1$ through $q$ are fusion cores, while those numbered $q+1$ through $2q$ are cooling towers. 

Engineers have tested $t$ different customized conduits. Each conduit is designed to bridge a specific fusion core to a specific cooling tower. You must choose a subset of these $t$ available conduits to permanently install. 

To ensure the ship's safety and functionality, your chosen installation must satisfy two non-negotiable requirements:
- **Total Integration**: Every fusion core and every cooling tower must be connected to the grid. Leaving any component unconnected will either cause a core meltdown or waste critical cooling capacity.
- **Strict Isolation**: No component can be attached to more than one conduit. Connecting multiple conduits to a single fusion core results in pressure loss, and connecting multiple conduits to a cooling tower causes it to overload.

Determine if there is a subset of the $t$ conduits that satisfies both requirements. If such an installation is possible, list the conduits to be installed. Otherwise, report that a safe layout cannot be achieved.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), denoting a certified conduit that can connect fusion core $a$ to cooling tower $b$.

## Output
If a safe layout is possible, output `YES` on the first line, followed by $q$ lines, each containing the two component identifiers of an installed conduit. If no such layout exists, output `NO`.

## Example

### Input
```
3 4
1 4
2 5
3 6
1 5
```

### Output
```
YES
1 4
2 5
3 6
```
