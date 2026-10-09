# Problem A — Station Configuration

Time limit: 5 s   Memory limit: 256 MB

## Description

A network switch needs to route data streams through three processing stages:
- **k** input ports, identified by integers 1 through **k**,
- **k** encryptors, identified by integers 1 through **k**,
- **k** output channels, identified by integers 1 through **k**.

You are provided with a routing table of **t** allowed paths. Each path is a triplet `(x, y, z)`, meaning input port **x** can connect to encryptor **y** and then to output channel **z**.

To fully utilize the switch, you must select exactly **k** paths from the routing table. A selection is considered a valid full-capacity configuration if and only if:
- When you extract the input port from each of the **k** chosen paths, the resulting list of **k** integers contains every number from 1 to **k** exactly once.
- When you extract the encryptor from each of the **k** chosen paths, the resulting list of **k** integers contains every number from 1 to **k** exactly once.
- When you extract the output channel from each of the **k** chosen paths, the resulting list of **k** integers contains every number from 1 to **k** exactly once.

Determine whether such a full-capacity configuration of exactly **k** paths can be formed. If it is possible, output one valid set of **k** paths.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of components in each stage and the number of allowed paths in the routing table.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing an allowed path. No path is listed more than once.

## Output

If a valid full-capacity configuration of exactly **k** paths exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen path. Any valid configuration is accepted; the paths may be printed in any order.

If no valid configuration exists, print `NO`.

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

In Example 2, both allowed paths use encryptor 1. If we select exactly 2 paths from this routing table, the list of extracted encryptors will consist of two `1`s. Since the list of used encryptors must contain all integers from 1 to 2 exactly once (meaning it must contain a `1` and a `2`), it is impossible to form a valid full-capacity configuration.