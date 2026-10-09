# Problem B — Thermal Controller Calibration

Time limit: 2 s   Memory limit: 256 MB

## Description
A manufacturing facility contains $q$ heat-producing modules (numbered $1$ through $q$) and $q$ thermal exhaust ports (numbered $q+1$ through $2q$). 

Coolant lines can only be established between specific module-port pairs due to physical obstructions in the facility's pressure hull. You are provided a blueprint detailing $t$ allowable coolant lines. Each allowable line connects one heat-producing module to one thermal exhaust port.

The thermal controller must activate a subset of these coolant lines to safely operate the facility. To prevent overheating, every heat-producing module must be connected to exactly one active coolant line. To prevent fluid overpressurization, every thermal exhaust port must be connected to exactly one active coolant line. 

Determine if a valid configuration exists using only the allowable lines from the blueprint. If a valid configuration is possible, output the lines to activate. If no such configuration exists, report that the facility cannot be safely operated.

## Input
The first line provides the number of modules/ports $q$ and the number of allowable lines $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing an allowable coolant line between module $a$ and exhaust port $b$.

## Output
If a valid configuration is possible, print `YES` on the first line, followed by $q$ lines each containing the two integers of an activated coolant line. If there are multiple valid configurations, you may output any of them.
If no valid configuration is possible, print `NO`.

## Example 1

### Input
```text
3 4
1 4
2 5
3 6
1 5
```

### Output
```text
YES
1 4
2 5
3 6
```

## Example 2

### Input
```text
3 2
1 4
2 5
```

### Output
```text
NO
```
