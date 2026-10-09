# Problem B — Thermal Dissipation Allocation

Time limit: 2 s   Memory limit: 256 MB

## Description
You are tasked with configuring the thermal dissipation system of a newly deployed orbital habitat. The habitat generates heat at $q$ distinct reactor nodes, which are sequentially indexed from $1$ up to $q$. This thermal energy must be routed to $q$ exterior cooling fins, which are indexed from $q+1$ up to $2q$.

Due to the station's rigid structural bulkheads, you cannot route any reactor to any cooling fin. The engineers have provided a manifest of $t$ structurally sound routing paths. Each path specifies one reactor node and one cooling fin that can be safely linked.

Your objective is to activate a subset of these routing paths such that every single reactor node is linked to exactly one cooling fin, and simultaneously, every single cooling fin is linked to exactly one reactor node. No reactor may share a fin, and no fin may service multiple reactors. Every asset (from $1$ to $2q$) must be utilized exactly once in the final configuration.

The manifest may contain many more paths than you will ultimately activate. A reactor might be part of several viable paths, and a fin might be part of several viable paths. However, you are restricted strictly to the exact combinations listed in the manifest. Decide whether the manifest admits such a complete one-to-one allocation of all reactors and fins. If it does, output one valid configuration; otherwise, report that the paths cannot simultaneously accommodate every asset.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating a viable routing path between reactor node $a$ and cooling fin $b$.

## Output
If a complete one-to-one configuration is possible, print `YES` on the first line, followed by $q$ lines each containing the two integers of an activated routing path. If there are multiple valid configurations, you may output any of them.
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
