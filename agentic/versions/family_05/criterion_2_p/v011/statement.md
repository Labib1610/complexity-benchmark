# Problem B — Backend Routing

Time limit: 2 s   Memory limit: 256 MB

## Description

A backend system is being deployed. The architecture consists of three sets of components, each containing exactly **k** elements:
- **k** API endpoints, numbered 1..k,
- **k** database shards, numbered 1..k,
- **k** IP addresses, numbered 1..k.

A valid routing configuration requires binding exactly one API endpoint and its corresponding database shard to a single IP address. You are provided with a list of allowed configurations, each given as a triplet `(e, d, i)`.

Due to the system's strict data partitioning, each API endpoint is hardcoded to query exactly one database shard, and no two endpoints query the same shard. Thus, the pairing between API endpoints and database shards is fixed by the system design. The only remaining task is to assign the IP addresses.

Your goal is to select exactly **k** configurations from the allowed list so that every API endpoint, every database shard, and every IP address is utilized in exactly one selected configuration. Determine if such a complete deployment is possible, and if so, output one valid selection.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of elements in each component set and the number of allowed routing configurations.
Each of the next **t** lines contains three integers **e**, **d**, **i** (1 ≤ e, d, i ≤ k), representing an allowed configuration. No configuration is listed more than once. For any given API endpoint, every listed configuration will specify the same database shard, and different API endpoints will always specify different database shards.

## Output

If a valid deployment of **k** configurations exists, print `YES` on the first line, then print **k** lines, each containing the three integers `e d i` of a selected configuration (the configurations may be printed in any order). Any valid deployment is acceptable.

If no valid deployment exists, print `NO`.

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
