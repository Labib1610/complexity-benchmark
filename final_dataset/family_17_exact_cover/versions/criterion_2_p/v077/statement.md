# Satellite Component Assembly

Time limit: 2 s   Memory limit: 256 MB

## Description
We have an inventory of $2q$ components for final satellite assembly. The components consist of exactly $q$ Control Modules (assigned IDs 1 through $q$) and $q$ Propulsion Units (assigned IDs $q+1$ through $2q$).

Final assembly requires joining one Control Module to one Propulsion Unit to form a complete satellite. Due to manufacturing tolerances, a module and a unit can only be joined if they have been physically verified to fit together. A verification log provides all $t$ compatible module-unit combinations.

The assembly schedule requires that every single component in the inventory is utilized. Furthermore, a component cannot be part of more than one assembled satellite. 

Determine if it is possible to assemble $q$ valid satellites such that every component is used exactly once. If it is possible, provide the exact pairing of components; otherwise, indicate that it is impossible.

## Input
The first line contains two integers $q$ and $t$ (1 ≤ $q$ ≤ 100000, 0 ≤ $t$ ≤ 400000), representing the number of components of each type and the number of verified combinations, respectively. 

The next $t$ lines each contain two integers $a$ and $b$ (1 ≤ $a$ ≤ $q$ < $b$ ≤ $2q$), representing a verified compatible combination between Control Module $a$ and Propulsion Unit $b$.

## Output
If it is possible to use all components exactly once in valid pairs, print `YES` on the first line. Then, print $q$ lines, each containing the two component IDs of an assembled satellite. If it is impossible, print `NO`.

## Example

### Input
```text
2 3
1 3
1 4
2 3
```

### Output
```text
YES
1 4
2 3
```
