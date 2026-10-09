# Problem B — Three-Tier Operational Logistics

Time limit: 2 s   Memory limit: 256 MB

## Description

A major industrial project requires the configuration of exactly **k** operational units. Each unit is a three-part assembly consisting of:

- A specialist (from a pool of **k** specialists, identified by IDs 1 through **k**)
- A piece of heavy machinery (from a pool of **k** machines, identified by IDs 1 through **k**)
- A deployment window (from a pool of **k** time slots, identified by IDs 1 through **k**)

You are provided with a comprehensive database of **t** authorized configurations. Each configuration is a triplet `(x, y, z)` denoting that specialist `x` can operate machine `y` during time slot `z`. 

Your objective is to find a perfect 3-dimensional subset: you must select exactly **k** configurations from the database such that every single specialist, every single machine, and every single time slot is deployed in exactly one chosen configuration. Satisfying these simultaneous, multi-dimensional constraints is necessary for the project to proceed. Note that in the provided database, all authorized configurations involving a particular specialist always feature the same machine, and no two specialists are associated with the same machine.

Determine if a valid configuration selection exists. If it does, report one such selection.

## Input

The first line provides two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k), representing the number of required units and the total number of authorized configurations.
Following this are **t** lines, each containing three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing an authorized configuration. No configuration is duplicated in the input. As described, any configuration containing specialist **x** will always pair them with their uniquely designated machine **y**, and no two specialists are paired with the same machine.

## Output

If it is possible to achieve a perfect configuration selection of **k** units, output `YES` on the first line. Then, output **k** lines, each containing the three integers `x y z` of a selected configuration. The configurations may be printed in any order. If multiple valid selections exist, any of them will be accepted.

If no such perfect selection is possible, output `NO`.

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
