# Precision Gear Synchronisation

Time limit: 5 s   Memory limit: 256 MB

## Description
A master watchmaker is designing a series of synchronisation mechanisms. The workshop contains a batch of exactly $3q$ unique micro-gears, individually engraved with a serial number from $1$ to $3q$.

A synchronisation mechanism requires exactly three distinct micro-gears to operate correctly. However, due to the intricate physics of the timepiece, not all combinations of three gears will function. The watchmaker has a reference log of $t$ known configurations that mesh perfectly.

Furthermore, a configuration is only considered stable if it meets three physical constraints:
- The span between the highest and lowest serial numbers in the configuration must be at least 2, to avoid harmonic resonance.
- The total sum of the three serial numbers must not exceed $9q - 3$, ensuring the rotational mass remains within safe limits.
- The product of the three serial numbers must be strictly less than $27q^3$, to prevent excessive friction.

Only stable configurations from the reference log can be used. The objective is to assemble exactly $q$ synchronisation mechanisms such that every single micro-gear from the batch is used exactly once. No micro-gear may be left over, and no micro-gear may be used in more than one mechanism.

Determine if there is a subset of stable configurations from the reference log that perfectly consumes the entire batch of $3q$ micro-gears. If so, provide the configurations to be used.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$).
The following $t$ lines each contain three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), detailing one known configuration of three micro-gears.

## Output
If the batch can be fully utilized under these conditions, print `YES` on the first line. Then, print $q$ lines, each containing the three micro-gears for one of the chosen configurations.
If it is impossible to use the batch completely following the constraints, print `NO`.

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
