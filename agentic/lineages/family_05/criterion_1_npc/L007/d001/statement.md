# Problem A — Drone Assembly Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description

A robotics facility is constructing a fleet of autonomous drones. The assembly line must produce exactly **k** functional units. The facility has exactly **k** items in each of three hardware categories:

- **k** chassis frameworks (identified by integers 1 through k)
- **k** navigation modules (identified by integers 1 through k)
- **k** imaging sensors (identified by integers 1 through k)

A single drone is assembled from exactly one chassis, one navigation module, and one imaging sensor. However, due to power and data-bus restrictions, only certain specific combinations of these three components can be successfully integrated. You are provided with a complete registry of all viable integration sets `(c, n, i)`.

To minimize waste and meet the production quota, the final assembly plan must incorporate every single chassis, every navigation module, and every imaging sensor into exactly one unit. You must choose exactly **k** viable integration sets from the registry such that no hardware component from any category is left unused or assigned to multiple drones.

Determine whether a complete assembly plan is possible, and if so, output the integration sets to be used. 

*Note on test data:* Be aware that the registry may be ordered adversarially. The official evaluation suite includes dense configurations containing many partial assembly plans that appear valid but inevitably fail near the final chassis assignment.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of items in each hardware category, and the total number of viable integration sets in the registry.
Each of the next **t** lines contains three integers **c**, **n**, **i** (1 ≤ c, n, i ≤ k), representing a viable integration set of chassis **c**, navigation module **n**, and imaging sensor **i**. No integration set is listed more than once in the registry.

## Output

If a valid assembly plan of **k** drones exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers `c n i` of a chosen integration set. Any selection that uses every chassis, navigation module, and imaging sensor exactly once will be accepted. You may print the chosen integration sets in any order.

If no valid assembly plan exists, print `NO`.

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

In Example 2, both viable integration sets require navigation module 1. Consequently, navigation module 2 can never be utilized, making a valid assembly plan impossible.