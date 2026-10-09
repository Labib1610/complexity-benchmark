# Fleet Assignment Scheduling

Time limit: 2 s
Memory limit: 256 MB

## Description
A logistics company must schedule exactly **k** deliveries. The schedule involves three sets of resources, each numbered 1 to **k**:
- **k** delivery routes,
- **k** specialized vehicles,
- **k** drivers.

A valid dispatch consists of one route, one vehicle, and one driver. You are provided a list of all feasible dispatches. Because of specific cargo requirements, each delivery route is strictly paired with exactly one specialized vehicle, and no two routes use the same vehicle.

Your goal is to select exactly **k** feasible dispatches such that every route, every vehicle, and every driver is assigned to exactly one dispatch. Determine if such a schedule is possible, and if so, output one valid set of dispatches.

## Input
The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k), representing the number of each resource type and the number of feasible dispatches.

Each of the next **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing a feasible dispatch of route **x**, vehicle **y**, and driver **z**. No dispatch is listed more than once. Consistent with the cargo requirements, all feasible dispatches for a given route specify the same vehicle, and different routes specify different vehicles.

## Output
If a complete schedule exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers `x y z` of a selected dispatch. The dispatches can be printed in any order. Any valid schedule is accepted.

If no complete schedule exists, print `NO`.

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
