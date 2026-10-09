# Problem A — Balanced Route Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description

You are tasked with deploying a perfectly balanced data processing network. The network architecture is designed to route continuous data streams from **k** data sources, through **k** transformer nodes, into **k** storage destinations. The components of each layer are indexed from 1 to **k**.

To maintain steady-state operation, data must be routed in unbroken triplets of `(source, transformer, destination)`. You are provided a list of **t** supported routes that have been verified for compatibility.

Your objective is to maximize network throughput by establishing a full-capacity routing assignment. This requires selecting exactly **k** routes to activate. The system achieves a perfectly balanced state if and only if every source, every transformer, and every destination is allocated to the active routes without omission or duplication. This strict load conservation ensures no component is left idle and no component acts as a bottleneck.

Determine if a full-capacity routing assignment is achievable, and if so, report the routes to activate.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of components of each layer, and the number of supported routes.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a supported route consisting of source **x**, transformer **y**, and destination **z**. No route is listed more than once.

## Output

If a perfectly balanced deployment of **k** routes exists, print `YES` on the first line, then print **k** lines, each containing the three integers `x y z` of one selected route. Any deployment where every source, transformer, and destination is utilized exactly once is accepted; the routes may be printed in any order.

If no such deployment exists, print `NO`.

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

In Example 2, both supported routes require transformer node 1, meaning transformer node 2 can never receive an assignment.
