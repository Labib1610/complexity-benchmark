# Problem B — Fleet Mobilization

Time limit: 2 s   Memory limit: 256 MB

## Description

The Galactic Defense Command is preparing for a major offensive that requires exactly $k$ independent task forces. The available resources consist of $k$ captains, $k$ cruisers, and $k$ target sectors, all indexed by integers from 1 to $k$.

A task force is formed by assigning one captain and one cruiser to one target sector. You have received a dossier containing $t$ authorized deployment configurations, each given as a triplet of a captain, a cruiser, and a sector.

The authorization process strictly enforces a one-to-one hardware binding between captains and cruisers. The dossier was compiled by establishing a master registry of $k$ exclusive captain-cruiser pairs (such that every captain is registered to exactly one cruiser, and every cruiser to exactly one captain), and then evaluating and authorizing various target sectors for each pair. Consequently, in the provided list of configurations, you will never see a captain associated with more than one cruiser, nor a cruiser associated with more than one captain.

Your objective is to activate exactly $k$ deployment configurations from the dossier such that every captain, every cruiser, and every target sector is utilized exactly once across the $k$ task forces. Determine if a full mobilization is possible, and if so, provide the chosen configurations.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 1200$, $0 \le t \le k \cdot k$), representing the number of available elements in each resource category and the total number of authorized configurations in the dossier.

The next $t$ lines each contain three integers $c$, $v$, and $s$ ($1 \le c, v, s \le k$), defining an authorized configuration of captain $c$, cruiser $v$, and sector $s$. All configurations in the input are unique. Following the hardware binding rules, any specific captain $c$ present in the input is paired with exactly one cruiser $v$ across all their configurations, and no two different captains are ever paired with the same cruiser.

## Output

If it is possible to form exactly $k$ task forces using every captain, cruiser, and sector exactly once, output `YES` on the first line. Following this, output $k$ lines, each containing the three integers $c$ $v$ $s$ of a selected configuration. The configurations can be printed in any order. If there are multiple valid mobilizations, any of them will be accepted.

If no such mobilization can be formed, output `NO`.

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
