# Problem A — Harmonic Resonance Clusters

Time limit: 5 s   Memory limit: 256 MB

## Description
A power station requires the activation of $q$ resonance generators. The station's inventory contains exactly $3q$ harmonic crystals, each assigned a unique serial number from $1$ to $3q$.

To activate a generator, engineers must install a cluster of exactly three crystals. For the station's grid to balance, every single crystal in the inventory must be installed into a generator, meaning each crystal is used exactly once.

Crystals feature unique frequency signatures and cannot be grouped at random. The engineers are provided with a list of $t$ certified clusters. Each certified cluster consists of three specific crystals that have been pre-tested to resonate safely. Any deviation from these pre-tested clusters will trigger a grid failure.

Evaluate the inventory and the list of certified clusters to find out if all $q$ generators can be activated.

## Input
The first line contains $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$), representing the number of generators and the number of certified clusters.
The next $t$ lines each contain three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), indicating the serial numbers of the crystals in a certified cluster.

## Output
If all generators can be activated, print `YES` on the first line. Then print $q$ lines, each detailing the three crystal serial numbers of a certified cluster used in the activation.
If it is impossible to activate all generators under these constraints, print `NO`.

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
