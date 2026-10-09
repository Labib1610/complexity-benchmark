# Problem B — Crew Assembly

Time limit: 2 s   Memory limit: 256 MB

## Description

A logistics planner is forming **k** independent work crews. There are three resource pools, each containing exactly **k** distinct elements:
- **k** specialists, identified by integers 1 through **k**,
- **k** machines, identified by integers 1 through **k**,
- **k** time slots, identified by integers 1 through **k**.

A complete crew is formed by selecting exactly one specialist, one machine, and one time slot. You are provided with a catalogue of viable crew configurations.

The catalogue was generated under strict equipment-assignment protocols: any given specialist only knows how to operate one specific machine, meaning every configuration in the catalogue involving a particular specialist will always feature the exact same machine. Furthermore, this equipment assignment is exclusive, meaning no machine will ever appear in configurations alongside more than one specialist.

Your goal is to select exactly **k** configurations from the catalogue such that every single specialist, every single machine, and every single time slot is scheduled in exactly one of the chosen crews. Determine whether such a selection is possible, and if so, report one valid set of crews.

## Input

The first line contains two integers **k** and **t** (1 ≤ **k** ≤ 1200, 0 ≤ **t** ≤ **k**·**k**), representing the size of each resource pool and the number of viable configurations in the catalogue.

Each of the subsequent **t** lines contains three integers **x**, **y**, and **z** (1 ≤ **x**, **y**, **z** ≤ **k**), representing a viable configuration consisting of specialist **x**, machine **y**, and time slot **z**. 

No configuration is duplicated in the list. The catalogue strictly adheres to the equipment-assignment protocols described above.

## Output

If a valid selection of **k** crews exists, print `YES` on the first line. Then, print **k** lines, each containing the three members **x** **y** **z** of one chosen crew (in any order). Any valid selection is accepted.

If no valid selection exists, print `NO`.

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
