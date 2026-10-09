# Orbital Station Assembly

Time limit: 2 s   Memory limit: 256 MB

## Description
An orbital station must be assembled from $2q$ prefabricated modules, identified by integers from 1 to $2q$.

The station's architecture requires grouping the modules into independent, two-module segments. To satisfy thermal dissipation regulations, each segment must pair exactly one power module (identifiers 1 through $q$) with exactly one habitation module (identifiers strictly greater than $q$). 

Modules can only be paired if their hardware interfaces are certified as compatible. The engineering registry lists $t$ such certified combinations.

Your objective is to integrate all $2q$ modules into segments such that no module is left unused, and no module is assigned to more than one segment. 

Determine whether a complete assembly is possible using only the certified combinations. If it is, provide the module pairs that form the segments; otherwise, indicate that the assembly cannot be completed.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing half the total number of modules and the number of certified combinations, respectively.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a certified combination between power module $a$ and habitation module $b$.

## Output
If a complete assembly is possible, print `YES` on the first line. Then, print $q$ lines, each containing the two module identifiers of a formed segment. If it is not possible, print `NO`.

## Example

**Input**
```text
3 5
1 4
1 5
2 5
3 5
3 6
```

**Output**
```text
YES
1 4
2 5
3 6
```
