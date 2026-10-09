# Problem B — Full-Coverage Network Activation

Time limit: 2 s   Memory limit: 256 MB

## Description
The facility's communication grid consists of $2q$ distinct nodes, uniquely identified by integers from $1$ to $2q$. For the upcoming stress test, the grid must be fully saturated.

To achieve saturation, you must activate a set of direct connections (channels) between the nodes. A master registry provides $t$ pre-certified channels, each specifying a pair of nodes that can successfully establish a stable connection. Your task is to select a subset of these channels such that every single node in the grid (from $1$ to $2q$) is an endpoint of exactly one activated channel from your selection. No node can be left isolated, and no node can participate in more than one active channel.

The registry's channels adhere to strict hardware isolation boundaries. For every certified channel connecting node $a$ and node $b$:
- Node $a$ is always from the lower tier ($1 \le a \le q$) and node $b$ is from the upper tier ($q < b \le 2q$).
- The sum of their identifiers, $a + b$, is guaranteed to be at least $q + 2$ and at most $3q$.
- The absolute difference between their identifiers, $b - a$, is guaranteed to be at least $1$.

Any channel not present in the registry cannot be activated. Determine if there is a valid selection of channels that fully saturates the grid. If so, output the selection. If no such selection exists, report the failure.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing half the total number of nodes, and the number of certified channels, respectively.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a certified channel between node $a$ and node $b$.

## Output
If a full saturation is possible, print `YES` on a single line, followed by $q$ lines, each containing the two nodes of an activated channel. If it is impossible, print `NO`.

## Example

**Input:**
```text
3 4
1 4
2 5
3 6
2 6
```

**Output:**
```text
YES
1 4
2 5
3 6
```
