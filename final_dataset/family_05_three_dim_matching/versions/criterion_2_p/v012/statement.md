# Problem B — Deployment Logistics

Time limit: 2 s
Memory limit: 256 MB

## Description

A logistics planner must organize exactly **k** deployments. There are three categories of resources available, each containing exactly **k** distinct elements:

- **k** agents, numbered 1 to k,
- **k** vehicles, numbered 1 to k,
- **k** sectors, numbered 1 to k.

A deployment consists of one agent, one vehicle, and one sector. You are provided with a log of successful test runs, each represented as a triplet `(agent, vehicle, sector)`.

The test runs were conducted under strict protocols. At the beginning of the testing phase, each of the **k** agents was permanently assigned to a seat in a different one of the **k** vehicles. Agents were not allowed to switch vehicles at any point. Throughout the testing phase, agents attempted to navigate various sectors. Every time an agent successfully completed a sector, the monitoring system logged the exact `(agent, vehicle, sector)` combination used.

Your task is to select exactly **k** combinations from the provided log such that every agent, every vehicle, and every sector is included in exactly one chosen deployment. Determine whether such a selection is possible, and if so, output one valid set of deployments.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of elements in each category and the number of logged successful test runs.
Each of the next **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing an agent, a vehicle, and a sector from a logged test run. No triplet is listed more than once. As a direct result of the testing protocols, all logged entries for a given agent feature the same vehicle, and no vehicle is featured in entries for more than one agent.

## Output

If a valid set of **k** deployments exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers `x y z` of one chosen deployment (in any order). If multiple valid sets exist, any of them will be accepted.

If no valid set exists, print `NO`.

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
