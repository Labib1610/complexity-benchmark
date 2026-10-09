# Problem B — Fleet Dispatch

Time limit: 2 s
Memory limit: 256 MB

## Description

A logistics company must complete $k$ delivery routes today using $k$ drivers and $k$ trucks. The operations manager has a list of pre-approved dispatch plans. Each dispatch plan specifies a driver, a truck, and a route.

In this fleet, each driver is permanently assigned to exactly one truck, and no two drivers share a truck. Therefore, any pre-approved plan involving a specific driver will always list their permanently assigned truck.

You must select exactly $k$ dispatch plans so that every driver, every truck, and every route is utilized exactly once. Determine if a valid schedule exists, and if so, output the selected plans.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 1200$, $0 \le t \le k \cdot k$): the number of each resource (drivers, trucks, routes) and the number of pre-approved dispatch plans.

Each of the following $t$ lines contains three integers $x$, $y$, and $z$ ($1 \le x, y, z \le k$) representing a dispatch plan consisting of driver $x$, truck $y$, and route $z$. No dispatch plan is listed more than once. For each driver, every listed plan uses the same truck, and different drivers use different trucks.

## Output

If a valid schedule of $k$ plans exists, print `YES` on the first line, then print $k$ lines, each containing the three integers $x$ $y$ $z$ of one selected plan. The plans may be printed in any order. Any valid schedule is accepted.

If no valid schedule exists, print `NO`.

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
