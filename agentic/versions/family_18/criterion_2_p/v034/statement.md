# Backbone Trenching Allocation

Time limit: 5 s
Memory limit: 256 MB

## Description
A monitoring installation consists of a set of sensors that must be installed along a straight trench. The trench features discrete mounting slots spaced at equal intervals. Every sensor requires exactly one mounting slot, and no slots can be left empty between sensors. Consequently, the slots used are numbered consecutively from 1 up to the total headcount of sensors.

Certain pairs of sensors must be directly wired together to exchange data. The wiring specifications are designed such that information can flow between any two sensors in the installation, but to minimize material costs, the total count of direct wire connections is strictly one less than the sensor headcount. This guarantees a single, unique path of wires between any two sensors.

When a wire connects a sensor placed in slot $X$ and a sensor placed in slot $Y$, the length of wire required is calculated as the absolute difference between $X$ and $Y$. The installation has a fixed allowance for the sum of all wire lengths used across the entire system.

You must determine if there is an assignment of sensors to slots that keeps the sum of all wire lengths within the given allowance.

## Input
The first line contains three integers $n$, $m$, and $B$.
- $n$ represents the headcount of sensors.
- $m$ represents the count of direct wire connections.
- $B$ represents the total wire length allowance.

Each of the following $m$ lines contains two integers $u$ and $v$, indicating a wire connecting the sensor identified as $u$ and the sensor identified as $v$ (where sensor identifiers range from 1 to the headcount).

## Output
If it is possible to assign the sensors to slots without exceeding the total allowance $B$, print `YES` on the first line. On the second line, print $n$ integers, where the $i$-th integer is the slot number assigned to sensor $i$. Each slot number from 1 up to the headcount must appear exactly once. If there are multiple valid assignments, output any of them.

If no such assignment is possible, print `NO`.

## Example
### Input
```
5 4 5
1 2
1 3
3 4
3 5
```
### Output
```
YES
2 1 3 4 5
```
