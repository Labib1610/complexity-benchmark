# Problem B — Telemetry Bridge Initialization

Time limit: 2 s
Memory limit: 256 MB

## Description
The initialization of the telemetry bridge requires selecting a precise subset of transmission links to activate. The system comprises $2q$ total communication endpoints, numbered $1$ to $2q$. The diagnostic scanner has compiled a whitelist of $t$ stable links between various pairs of endpoints.

To establish a full-capacity bridge, you must search the configuration space to find a set of exactly $q$ links such that every single endpoint from $1$ to $2q$ is committed to exactly one selected link. With up to $400,000$ stable links and a requirement to select exactly $100,000$ of them, the number of possible subset combinations is astronomically large. You must determine if a valid subset exists that incorporates all endpoints without any overlap. If a valid configuration exists, the physical controller will lock it in. If the entire search space yields no valid configuration, the system must enter safe mode.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), where $2q$ is the total number of endpoints and $t$ is the number of stable links.

The next $t$ lines describe the whitelist of stable links. Each line contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a stable transmission link between endpoint $a$ and endpoint $b$. For hardware reasons, endpoints $1$ through $q$ are physically located in ground arrays, while endpoints $q+1$ through $2q$ are situated in orbital relays.

## Output
If a full-capacity bridge can be formed, print `YES` on the first line, followed by $q$ lines each containing the two IDs of an activated link. If it is impossible to commit every endpoint exactly once, print `NO`.

## Example

**Input**
```
3 4
1 4
2 5
2 6
3 6
```

**Output**
```
YES
1 4
2 5
3 6
```
