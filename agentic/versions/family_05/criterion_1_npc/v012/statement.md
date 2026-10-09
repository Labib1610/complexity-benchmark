# Problem A — Probe Launch Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description

A space agency is preparing to launch a fleet of **k** deep-space probes. The agency's inventory contains exactly **k** power cores, **k** navigation units, and **k** communication arrays. Within each category, the components are assigned serial numbers from 1 to **k**.

A functioning probe requires exactly one power core, one navigation unit, and one communication array. However, due to hardware quirks, only certain specific combinations of components can be stabilized together. You are provided with a catalog of **t** stable configurations. Each configuration is defined by a triplet of serial numbers `(x, y, z)` corresponding to a power core, a navigation unit, and a communication array, respectively.

Your objective is to authorize exactly **k** configurations from the catalog to build the **k** probes. Because each component physically exists only once in the inventory, no individual power core, navigation unit, or communication array may be assigned to more than one probe. 

Determine if it is possible to successfully build all **k** probes, and if so, provide one valid set of configurations.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k), representing the number of probes to build (which also dictates the inventory size for each component type) and the number of stable configurations in the catalog.

Each of the next **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing a stable configuration consisting of power core **x**, navigation unit **y**, and communication array **z**. No configuration is duplicated in the catalog.

## Output

If it is possible to authorize exactly **k** configurations under the given constraints, output `YES` on the first line. Then, output **k** lines, each containing the three serial numbers `x y z` of an authorized configuration. The configurations can be printed in any order. If multiple valid authorizations exist, any one that uses every component exactly once is acceptable.

If no such authorization is possible, output `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
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
2 1 2
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

## Note

In Example 2, both stable configurations require navigation unit 1. Consequently, navigation unit 2 can never be utilized, making it impossible to build both probes.
