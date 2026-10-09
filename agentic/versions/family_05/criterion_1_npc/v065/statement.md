# Synaptic Core Initialization

Time limit: 5 s   Memory limit: 256 MB

## Description

A cybernetics lab is attempting to initialize a neural matrix consisting of exactly **k** synaptic cores. The initialization requires three distinct types of stimuli: **k** pulse frequencies, **k** routing pathways, and **k** activation thresholds. Each individual stimulus is identified by an integer from 1 to **k**.

A synaptic core is stabilized by linking it with exactly one pulse frequency, one routing pathway, and one activation threshold. However, due to resonance conflicts, only certain specific triplets of (frequency, pathway, threshold) can safely stabilize a core. You will be given the complete registry of all safe triplets.

The neural matrix is considered fully initialized if and only if every pulse frequency is assigned to some core, every routing pathway is assigned to some core, and every activation threshold is assigned to some core.

The lab's containment parameters guarantee two structural properties for any given registry:
- The total number of safe triplets in the registry is at most 10,648.
- For any safe triplet, the sum of its three stimulus identifiers will not exceed 66.

Determine whether it is possible to select exactly **k** safe triplets that successfully initialize the matrix. If a valid selection exists, output one such selection.

## Input

The first line provides two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k³): the number of synaptic cores (which equals the number of available stimuli in each category) and the number of safe triplets in the registry.

Each of the following **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing a safe triplet consisting of pulse frequency **x**, routing pathway **y**, and activation threshold **z**. All listed triplets are distinct.

## Output

If there is a valid selection of **k** triplets that initializes the matrix, output `YES` on the first line. Following that, output **k** lines, each containing the three integers `x y z` of one selected triplet. Any valid selection is acceptable, and the selected triplets may be printed in any order.

If no such selection is possible, output `NO`.

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
