# Problem B — Operation Schedules

Time limit: 2 s   Memory limit: 256 MB

## Description

An aviation company needs to finalize **k** flight manifestos. The company has exactly **k** captains, **k** jets, and **k** destinations, each identified by an integer from 1 to **k**.

A manifesto is formed by a triplet consisting of a captain, a jet, and a destination. You will receive a catalog of **t** cleared triplets. 

Due to strict operational protocols, a captain is exclusively trained for a single jet, and each jet is assigned to a unique captain. Consequently, throughout the catalog of cleared triplets, a specific captain will always appear with the same jet, and no jet will be associated with more than one captain. 

You must select exactly **k** triplets from the catalog to form a complete schedule. A schedule is valid if and only if every captain, every jet, and every destination appears exactly once across the selected manifestos. Determine if such a schedule can be formed, and if so, report the chosen triplets.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k), representing the count for each resource type and the number of cleared triplets.

The following **t** lines each contain three integers **c**, **j**, and **d** (1 ≤ c, j, d ≤ k), representing a cleared triplet of a captain, a jet, and a destination. All triplets in the input are distinct. As per the operational protocols, any triplet containing captain **c** will feature the same jet **j**, and no two different captains will appear with the same jet.

## Output

If a complete schedule exists, print `YES` on the first line. Then, output **k** lines, each containing the three integers `c j d` of a selected triplet (in any order). Any valid schedule is accepted.

If no complete schedule can be formed, print `NO`.

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

## Note

In Example 2, both captains are only cleared for destination 1, leaving destination 2 impossible to reach.
