# Problem B — Material Synthesis

Time limit: 2 s   Memory limit: 256 MB

## Description

You are tasked with operating a synthesizer to produce a novel material. This requires running exactly **k** distinct chemical processes concurrently. Each individual process must be fueled by a triplet of components:
- One core unit
- One modulator unit
- One stabilizer unit

All components are assigned integer identifiers starting from 1 up to **k**.

You have access to a catalog of **t** known stable triplets. Each entry specifies a core, a modulator, and a stabilizer that can safely react together.

Because of stringent molecular constraints, a specific core unit can only ever function with one unique modulator unit. Consequently, in the catalog, any given core is always paired with the exact same modulator. Furthermore, this relationship is strictly exclusive: no modulator is ever associated with more than one core. 

Your objective is to pick exactly **k** triplets from the catalog to run the **k** processes. To ensure a balanced reaction, every core unit (from 1 to **k**), every modulator unit (from 1 to **k**), and every stabilizer unit (from 1 to **k**) must be used exactly once across the chosen processes. 

Identify whether safely configuring the synthesizer is possible. If it is, output a valid selection of triplets.

## Input

The first line contains two integers **k** and **t**. The capacity of the synthesizer's physical bays limits the process count **k** to a maximum of 1200 (with a minimum requirement of 1). The catalog size **t** ranges from an empty record (0) up to the theoretical maximum where every exclusive core-modulator pair is matched with every available stabilizer.

Each of the subsequent **t** lines contains three integers **x**, **y**, and **z**, denoting a stable triplet made of core **x**, modulator **y**, and stabilizer **z**. The identifiers are strictly bounded between the lowest valid label (1) and the maximum label (**k**). All catalog entries are distinct. The catalog respects the exclusive pairing rule: any core appears with only one specific modulator, and different cores appear with different modulators.

## Output

If there is a valid selection of **k** processes, print `YES` on the first line. Then, print **k** lines, each containing the three integers `x y z` representing a chosen triplet. The chosen triplets can be printed in any order. Any valid selection is acceptable.

If no such selection can be made, print `NO`.

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
