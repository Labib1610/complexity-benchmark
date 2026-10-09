# Orbital Thermal Management

Time limit: 2 s   Memory limit: 256 MB

## Description
You are configuring the active thermal management system for an orbital facility. The system contains $q$ heat-generating instrument bays, sequentially indexed from $1$ to $q$. The heat from these bays must be transferred to $q$ exterior radiator panels, sequentially indexed from $q+1$ to $2q$. 

Because of the facility's internal geometry, a coolant loop can only be established between specific pairs of instrument bays and radiator panels. You are given a list of $t$ structurally cleared conduits, each capable of forming a single coolant loop between one bay and one panel. 

Your task is to select a subset of these conduits to activate such that every instrument bay is assigned to exactly one radiator panel, and every radiator panel is assigned to exactly one instrument bay. If such a configuration exists, output the list of selected loops; otherwise, report that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating a cleared conduit that can form a loop between instrument bay $a$ and radiator panel $b$.

## Output
If a complete configuration is possible, print `YES` on the first line, followed by $q$ lines each containing the two integers of an activated conduit. If there are multiple valid configurations, you may output any of them.
If no such configuration is possible, print `NO`.

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
