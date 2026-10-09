# Problem A — Resource Alignment

Time limit: 5 s   Memory limit: 256 MB

## Description

In a secure facility, workflows are built from authorized operational profiles. An operational profile is defined by a specific triplet: an operator, a hardware terminal, and a duty shift. You are given a catalog of **t** such authorized profiles. 

When activating a collection of profiles from this catalog, strict isolation protocols apply. If multiple profiles are activated simultaneously, they must be entirely disjoint in their resource usage. This means no operator may appear in more than one activated profile, no hardware terminal may be used in more than one activated profile, and no duty shift may be associated with more than one activated profile. 

The facility possesses exactly **k** operators, **k** hardware terminals, and **k** duty shifts, with the items in each category identified by integers from 1 to **k**. For a scheduled deployment to be considered complete, it must activate exactly **k** profiles such that every single available operator, terminal, and shift is engaged exactly once. 

Determine whether there exists a valid collection of profiles from the catalog that can be activated together to achieve a complete deployment. If it is possible, provide one such collection.

## Input

The first line provides two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k³), representing the quantity of each resource type and the number of authorized profiles in the catalog.

Each of the subsequent **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k). These denote an authorized profile comprising operator **x**, terminal **y**, and shift **z**. All profiles in the catalog are guaranteed to be distinct.

## Output

If a complete deployment is possible, output `YES` on the first line. Following this, output **k** lines, each containing three integers `x y z` representing one of the activated profiles. The profiles may be output in any sequence. If multiple valid complete deployments exist, any of them will be accepted.

If no complete deployment is possible, output `NO`.

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

In Example 2, both authorized profiles require terminal 1. Because of the isolation protocols, terminal 2 can never be utilized, making a complete deployment impossible.
