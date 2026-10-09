# Problem B — Resource Pipeline Commissioning

Time limit: 2 s   Memory limit: 256 MB

## Description

The planetary resource extraction lifecycle consists of three distinct phases: surveying, pipeline commissioning, and orbital shipping. 

In Phase 1, geological surveyors identify exactly **k** extraction sites. These sites produce raw materials that must be refined and stored. 

This brings us to Phase 2, which you are responsible for. The infrastructure for Phase 2 requires assembling pipelines from three sets of components, each containing exactly **k** elements:
- **k** extraction sites, numbered 1..k,
- **k** distillation columns, numbered 1..k,
- **k** injection wells, numbered 1..k.

A valid pipeline blueprint binds one extraction site and its associated distillation column to a single injection well. You receive a manifest of approved blueprints, each represented as a triplet `(e, d, i)`. 

Due to the chemical signatures analyzed during Phase 1, each extraction site is exclusively compatible with one specific distillation column, and no two extraction sites can share the same distillation column. Consequently, the pairing between extraction sites and distillation columns is strictly predetermined by the approved blueprints. Your task for Phase 2 is to finalize the pipelines by assigning the injection wells. You must select exactly **k** blueprints from the manifest such that every extraction site, every distillation column, and every injection well is incorporated into exactly one selected blueprint.

Once Phase 2 is successfully commissioned, Phase 3 begins, where the stabilized resources from the injection wells are loaded onto freighters for orbital shipping. 

Determine if a complete Phase 2 commissioning is possible, and if so, output one valid selection of blueprints.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of elements in each component set and the total number of approved blueprints in the manifest.
Each of the next **t** lines provides three integers **e**, **d**, **i** (1 ≤ e, d, i ≤ k), representing a single approved blueprint. No blueprint is listed more than once. For any given extraction site, every listed blueprint will specify the same distillation column, and different extraction sites will always specify different distillation columns.

## Output

If a valid Phase 2 commissioning of **k** blueprints exists, print `YES` on the first line, then print **k** lines, each containing the three integers `e d i` of a selected blueprint (the blueprints may be printed in any order). Any valid commissioning is acceptable.

If no valid commissioning exists, print `NO`.

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
