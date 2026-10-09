# Horological Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description
A boutique watchmaker is designing complication modules using a limited stock of distinct micro-gears. The inventory holds exactly $3q$ micro-gears. Each micro-gear is stamped with a unique serial number ranging from $1$ to $3q$ inclusive.

The watchmaker must assemble these gears into complication modules. Each module is built from exactly three micro-gears. However, due to complex mechanical dependencies, gears cannot be grouped arbitrarily. The watchmaker has a catalog of $t$ tested schematics. Each schematic specifies a working triplet of three unique micro-gears that mesh correctly. (Due to spatial tolerances within the watch casing, any schematic in the catalog is guaranteed to have the sum of its three gear serial numbers never exceed $9q - 3$.)

The goal is to process the inventory into a batch of modules with zero waste. A valid production run must satisfy the following strict certification requirements:
1. Every micro-gear in the inventory must be incorporated into exactly one module (no gear is left unused, and no gear is used more than once).
2. To ensure perfect rotational weight distribution, the total sum of the serial numbers of all micro-gears across all modules in the production run must equal exactly $3q(3q+1)/2$.
3. The production run must consist of exactly $q$ modules.

Determine if it is possible to select a set of schematics from the catalog that fulfills all certification requirements. If such a production run is possible, you must output the chosen schematics.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
The following $t$ lines each provide three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing one tested schematic of three micro-gears available in the catalog.

## Output
If the inventory can be fully utilized according to the certification requirements, print `YES` on the first line. Then, print $q$ lines, each containing the three micro-gears for one of the chosen schematics.
If no valid production run exists, print `NO`.

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
