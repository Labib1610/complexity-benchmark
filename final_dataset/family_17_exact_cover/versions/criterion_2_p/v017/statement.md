# Problem B — Telemetry Bridge Initialization

Time limit: 2 s
Memory limit: 256 MB

## Description
The initialization of the telemetry bridge requires completing three distinct phases. 

**Phase 1: Diagnostic Scanning (Complete)**
The system contains $q$ ground arrays (assigned IDs $1$ to $q$) and $q$ orbital relays (assigned IDs $q+1$ to $2q$). The diagnostic scanner has already tested all possible connections and compiled a whitelist of $t$ stable transmission links. Each stable link connects one ground array to one orbital relay. 

**Phase 2: Core Allocation (Your Task)**
You must process the whitelist from Phase 1 to establish a full-capacity bridge. A full-capacity bridge requires activating a subset of the stable links such that *every* ground array and *every* orbital relay is committed to exactly one active link. No array or relay may be left idle, and no array or relay may be assigned to multiple links. You must determine if such a configuration exists and, if so, output the chosen links.

**Phase 3: Phase Modulation (Pending)**
If your allocation is successful, the downstream physical controller will lock the links you selected and begin phase modulation. If you determine that no full-capacity bridge can be formed, the system will abort and enter safe mode. You only need to execute Phase 2.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of ground arrays (which is also the number of orbital relays) and the number of stable links found in Phase 1.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a stable transmission link between ground array $a$ and orbital relay $b$.

## Output
If a full-capacity bridge can be formed, print `YES` on the first line, followed by $q$ lines each containing the two IDs of an activated link. If it is impossible to commit every array and relay exactly once, print `NO`.

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
