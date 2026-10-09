# Problem A — Harmonic Resonance Clusters

Time limit: 5 s   Memory limit: 256 MB

## Description
The facility's inventory is stocked with exactly $3q$ resonance modules, each stamped with a unique identifier from $1$ to $3q$. These modules exhibit distinct frequency profiles. Through rigorous testing, engineers have compiled a safety catalog containing $t$ stable triplets. A stable triplet is a specific combination of exactly three resonance modules that can operate together without causing destructive interference.

The facility houses $q$ reactors. A reactor operates safely only when loaded with one stable triplet from the catalog. The facility's power balancing protocols mandate that the entire inventory of modules must be utilized across the reactors, meaning every single module from $1$ to $3q$ must be placed into a reactor exactly once.

Your task is to evaluate the inventory and the safety catalog to determine whether the $q$ reactors can be brought online simultaneously under these protocols, and if so, to provide a valid loading configuration.

## Input
The first line provides $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), which are the number of reactors and the number of stable triplets in the safety catalog, respectively.
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), specifying the identifiers of the modules that form a stable triplet.

## Output
If it is possible to bring all reactors online while adhering to the protocols, print `YES` on the first line. Following this, print $q$ lines, each containing the three module identifiers of a stable triplet used to load a reactor.
If there is no valid configuration that satisfies the protocols, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
